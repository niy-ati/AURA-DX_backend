from pydantic import BaseModel
from typing import List, Optional, Dict, Any

class BaselineMetrics(BaseModel):
    status: str
    confidence: float

class BaselineData(BaseModel):
    shortTerm: BaselineMetrics
    midTerm: BaselineMetrics
    longTerm: BaselineMetrics

class ContextualFactors(BaseModel):
    stress: str
    stressScore: float
    sleep: str
    sleepQuality: float
    activity: str
    stepCount: int
    recentTravel: bool
    caffeineIntake: str
    circadianPhase: str

class RppgData(BaseModel):
    lastCapture: str
    captureQuality: float
    lightingScore: float
    motionStability: float
    signalStrength: str
    captureCount: int

class CoughAnalysis(BaseModel):
    lastRecording: str
    audioQuality: Optional[float]
    coughDetected: bool
    features: Optional[Dict[str, str]]
    spectralAnalysis: Optional[Dict[str, Any]]
    riskFlags: List[str]

class Patient(BaseModel):
    id: str
    name: str
    age: int
    gender: str
    phone: str
    deviceType: str
    deviceConnected: bool
    lastSync: str
    riskScore: int
    riskLevel: str
    confidence: float
    baselineStatus: str
    anomalyDetected: bool
    anomalyType: Optional[str]
    evidenceGating: str
    sensorQuality: float
    heartRate: int
    hrv: int
    respiratoryRate: int
    consent: Dict[str, bool]
    encryptionStatus: str
    baseline: BaselineData
    baselinePhase: str
    contextualFactors: ContextualFactors
    rppgData: RppgData
    coughAnalysis: CoughAnalysis
    diseaseFlags: List[Dict[str, Any]]
    riskClusters: List[Dict[str, Any]]
    alerts: List[Dict[str, Any]]
    passiveSignals: Dict[str, Any]
    sensorHistory: List[Dict[str, Any]]
    evidenceTimeline: List[Dict[str, Any]]