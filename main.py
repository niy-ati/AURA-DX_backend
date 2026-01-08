from fastapi import FastAPI, WebSocket, WebSocketDisconnect, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware
import shutil
import os
import json

from database import patients_db
from intelligence import process_rppg_signal, analyze_cough_file

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

class ConnectionManager:
    def __init__(self):
        self.active_connections: list[WebSocket] = []
    async def connect(self, ws: WebSocket):
        await ws.accept()
        self.active_connections.append(ws)
    def disconnect(self, ws: WebSocket):
        self.active_connections.remove(ws)
    async def broadcast(self, message: dict):
        for conn in self.active_connections:
            await conn.send_json(message)

manager = ConnectionManager()

@app.get("/patients")
def get_patients():
    return patients_db

@app.post("/context/{patient_id}")
async def update_context(patient_id: str, data: dict):
    for p in patients_db:
        if p["id"] == patient_id:
            p["contextualFactors"].update(data)
            p["evidenceTimeline"].insert(0, {
                "time": "Just now",
                "event": "Passive context updated",
                "type": "gating"
            })
    await manager.broadcast({"type": "UPDATE_PATIENTS", "data": patients_db})
    return {"status": "Context Updated"}

@app.post("/baseline/recalibrate/{patient_id}")
async def recalibrate_baseline(patient_id: str):
    for p in patients_db:
        if p["id"] == patient_id:
            p["baselinePhase"] = "Recalibrated (Stable)"
            p["baseline"]["shortTerm"]["status"] = "Reset"
            p["evidenceTimeline"].insert(0, {
                "time": "Just now",
                "event": "Clinician approved baseline recalibration",
                "type": "alert"
            })
    await manager.broadcast({"type": "UPDATE_PATIENTS", "data": patients_db})
    return {"status": "Recalibration Complete"}

@app.post("/analyze/cough/{patient_id}")
async def analyze_cough(patient_id: str, file: UploadFile = File(...)):
    temp_name = f"temp_{file.filename}"
    with open(temp_name, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)
    
    results = analyze_cough_file(temp_name)
    os.remove(temp_name)
    
    for p in patients_db:
        if p["id"] == patient_id:
            p["coughAnalysis"]["spectrogram_image"] = results.get("spectrogram_image")
            p["evidenceTimeline"].insert(0, {
                "time": "Just now",
                "event": "New Cough Analysis Available",
                "type": "analysis"
            })
    
    await manager.broadcast({"type": "UPDATE_PATIENTS", "data": patients_db})
    return results

@app.websocket("/ws/rppg/{patient_id}")
async def rppg_endpoint(websocket: WebSocket, patient_id: str):
    await websocket.accept()
    buffer = []
    try:
        while True:
            data = await websocket.receive_json()
            buffer.append(data["value"])
            
            if len(buffer) > 90:
                results = process_rppg_signal(buffer[-90:])
                if results:
                    await websocket.send_json(results)
                if len(buffer) > 300: buffer = buffer[-90:]
    except WebSocketDisconnect:
        print(f"rPPG Disconnected for {patient_id}")

@app.websocket("/ws")
async def dashboard_socket(websocket: WebSocket):
    await manager.connect(websocket)
    try:
        while True: await websocket.receive_text()
    except: manager.disconnect(websocket)