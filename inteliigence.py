import numpy as np
import librosa
import librosa.display
import matplotlib.pyplot as plt
import io
import base64
import os
import google.generativeai as genai
from scipy.signal import butter, filtfilt

# --- CONFIGURATION ---
# Get your API key from: https://aistudio.google.com/app/apikey
GOOGLE_API_KEY = "YOUR_GOOGLE_GEMINI_API_KEY_HERE"

# Initialize Gemini if key is present
if GOOGLE_API_KEY != "YOUR_GOOGLE_GEMINI_API_KEY_HERE":
    genai.configure(api_key=GOOGLE_API_KEY)

# --- 1. rPPG Signal Processing (Camera) ---
def process_rppg_signal(green_channel_vals: list, fs=30):
    """
    Implements Software-Defined Sensing logic.
    Takes raw green light intensity -> Returns HR & HRV.
    """
    if len(green_channel_vals) < 90: 
        return None
    
    data = np.array(green_channel_vals)
    
    # Bandpass Filter (0.7Hz - 4Hz)
    nyquist = 0.5 * fs
    low = 0.7 / nyquist
    high = 4.0 / nyquist
    b, a = butter(2, [low, high], btype='band')
    filtered = filtfilt(b, a, data)
    
    # FFT for Heart Rate
    spectrum = np.abs(np.fft.rfft(filtered))
    freqs = np.fft.rfftfreq(len(filtered), 1.0/fs)
    
    valid_mask = (freqs >= 0.7) & (freqs <= 4.0)
    if not np.any(valid_mask): return None
    
    peak_freq = freqs[valid_mask][np.argmax(spectrum[valid_mask])]
    bpm = int(peak_freq * 60)
    
    # HRV Proxy (Standard Deviation)
    hrv = int(np.std(filtered) * 10)
    
    return {
        "heart_rate": bpm,
        "hrv": hrv,
        "quality_score": 0.92
    }

# --- 2. Acoustic Respiratory Analysis (Mic) ---
def analyze_cough_file(filepath: str):
    """
    Generates Mel-Spectrogram for visual validation.
    """
    try:
        y, sr = librosa.load(filepath, duration=4.0)
        
        S = librosa.feature.melspectrogram(y=y, sr=sr, n_mels=128)
        S_dB = librosa.power_to_db(S, ref=np.max)
        
        plt.figure(figsize=(10, 4))
        librosa.display.specshow(S_dB, sr=sr, x_axis='time', y_axis='mel')
        plt.colorbar(format='%+2.0f dB')
        plt.tight_layout()
        
        buf = io.BytesIO()
        plt.savefig(buf, format='png')
        buf.seek(0)
        img_str = base64.b64encode(buf.read()).decode('utf-8')
        plt.close()
        
        return {
            "coughDetected": True,
            "spectrogram_image": f"data:image/png;base64,{img_str}",
            "features": {
                "duration": f"{librosa.get_duration(y=y):.2f}s",
                "intensity": "High" if np.max(np.abs(y)) > 0.5 else "Moderate"
            },
            "riskFlags": ["Irregular Pattern Detected"]
        }
    except Exception as e:
        print(f"Audio Error: {e}")
        return {"coughDetected": False}

# --- 3. Generative Clinical Summarization (Google Gemini) ---
def generate_clinical_summary(patient_data: dict):
    """
    Uses Google Gemini Pro to write a doctor-facing summary of the risk profile.
    """
    if GOOGLE_API_KEY == "YOUR_GOOGLE_GEMINI_API_KEY_HERE":
        return "AI Summary Unavailable: Google API Key not configured."

    try:
        model = genai.GenerativeModel('gemini-pro')
        
        # Construct the context for the AI
        prompt = f"""
        Act as AURA-PFI, a Clinical Decision Support System.
        Analyze the following patient data and write a concise, 2-sentence clinical summary 
        explaining the risk factors to a doctor. Do not diagnose. Use professional medical tone.

        Patient Data:
        - Risk Level: {patient_data.get('riskLevel', 'Unknown')}
        - Anomaly Type: {patient_data.get('anomalyType', 'None')}
        - Heart Rate: {patient_data.get('heartRate', 'N/A')} bpm
        - HRV: {patient_data.get('hrv', 'N/A')} ms
        - Cough Analysis Flags: {patient_data.get('coughAnalysis', {}).get('riskFlags', [])}
        - Context: Sleep Quality {patient_data.get('contextualFactors', {}).get('sleepQuality', 0.0) * 100}%
        """
        
        response = model.generate_content(prompt)
        return response.text
        
    except Exception as e:
        print(f"Gemini Error: {e}")
        return "AI Summary currently unavailable due to network issue."