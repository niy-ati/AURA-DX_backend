patients_db = [
    {
        "id": "P001",
        "name": "Rohan Sharma",
        "age": 34,
        "gender": "Male",
        "phone": "+91 98765 43210",
        "deviceType": "Samsung Galaxy S23",
        "deviceConnected": True,
        "lastSync": "2 min ago",
        "riskScore": 78,
        "riskLevel": "High",
        "confidence": 0.87,
        "baselineStatus": "Stable",
        "anomalyDetected": True,
        "anomalyType": "Persistent Chest Instability",
        "evidenceGating": "Respiratory Analysis Active",
        "sensorQuality": 0.92,
        "heartRate": 89,
        "hrv": 42,
        "respiratoryRate": 19,
        "consent": { "camera": True, "microphone": True, "wearable": True, "cloudProcessing": True },
        "encryptionStatus": "AES-256 Active",
        "baseline": {
            "shortTerm": { "status": "Deviation Detected", "confidence": 0.89 },
            "midTerm": { "status": "Under Review", "confidence": 0.76 },
            "longTerm": { "status": "Normal Aging Pattern", "confidence": 0.94 }
        },
        "baselinePhase": "Long-Term Stabilized",
        "rppgData": {
            "lastCapture": "5 min ago",
            "captureQuality": 0.94,
            "lightingScore": 0.91,
            "motionStability": 0.96,
            "signalStrength": "Excellent",
            "captureCount": 247
        },
        "coughAnalysis": {
            "lastRecording": "12 min ago",
            "audioQuality": 0.88,
            "coughDetected": True,
            "features": {
                "frequency": "Abnormal High",
                "duration": "280ms (Prolonged)",
                "intensity": "Moderate-High",
                "pattern": "Irregular intervals"
            },
            "spectralAnalysis": {
                "mfcc": [0.82, 0.76, 0.91, 0.68],
                "melSpectrogram": "Atypical pattern detected"
            },
            "riskFlags": ["Respiratory Obstruction Pattern", "Potential Airway Inflammation"]
        },
        "diseaseFlags": [
            { "condition": "Respiratory Distress", "probability": 0.82, "severity": "High", "evidence": ["Abnormal cough pattern", "Elevated respiratory rate", "HRV decline"] },
            { "condition": "Cardiovascular Stress", "probability": 0.68, "severity": "Medium", "evidence": ["Elevated HR", "Low HRV", "Baseline drift"] }
        ],
        "riskClusters": [
            { "category": "Cardiovascular", "probability": 0.68, "contributing": ["Elevated HR", "Low HRV"] },
            { "category": "Respiratory", "probability": 0.82, "contributing": ["Cough Pattern Abnormal", "Breath Irregularity"] }
        ],
        "alerts": [
            { "id": "A001", "severity": "High", "message": "Persistent anomaly detected - Respiratory analysis required", "timestamp": "10 min ago", "status": "Pending", "requiresAction": True }
        ],
        "contextualFactors": {
            "stress": "Moderate",
            "stressScore": 6.2,
            "sleep": "5.2 hrs (Low)",
            "sleepQuality": 0.42,
            "activity": "Sedentary",
            "stepCount": 3200,
            "recentTravel": False,
            "caffeineIntake": "High (3 cups today)",
            "circadianPhase": "Misaligned"
        },
        "passiveSignals": {
            "phoneUsagePattern": "Increased (Stress indicator)",
            "sleepConsistency": "Irregular",
            "movementPattern": "Reduced 40%",
            "screenTime": "8.2 hrs",
            "lastBackgroundAlert": "18 hours ago"
        },
        "sensorHistory": [],
        "evidenceTimeline": [
            { "time": "09:16 AM", "event": "Anomaly detected in cardiovascular baseline", "type": "detection" },
            { "time": "09:27 AM", "event": "Alert generated - Awaiting clinician confirmation", "type": "alert" }
        ]
    },
    {
        "id": "P002",
        "name": "Priya Patel",
        "age": 28,
        "gender": "Female",
        "phone": "+91 98123 45678",
        "deviceType": "iPhone 14 Pro",
        "deviceConnected": True,
        "lastSync": "5 min ago",
        "riskScore": 34,
        "riskLevel": "Low",
        "confidence": 0.91,
        "baselineStatus": "Stable",
        "anomalyDetected": False,
        "anomalyType": None,
        "evidenceGating": "Inactive - All systems normal",
        "sensorQuality": 0.96,
        "heartRate": 68,
        "hrv": 64,
        "respiratoryRate": 14,
        "consent": { "camera": True, "microphone": True, "wearable": True, "cloudProcessing": True },
        "encryptionStatus": "AES-256 Active",
        "baseline": {
            "shortTerm": { "status": "Normal", "confidence": 0.95 },
            "midTerm": { "status": "Normal", "confidence": 0.93 },
            "longTerm": { "status": "Normal", "confidence": 0.96 }
        },
        "baselinePhase": "Long-Term Stabilized",
        "rppgData": {
            "lastCapture": "3 min ago",
            "captureQuality": 0.97,
            "lightingScore": 0.95,
            "motionStability": 0.98,
            "signalStrength": "Excellent",
            "captureCount": 189
        },
        "coughAnalysis": {
            "lastRecording": "Not required",
            "audioQuality": None,
            "coughDetected": False,
            "features": None,
            "spectralAnalysis": None,
            "riskFlags": []
        },
        "diseaseFlags": [],
        "riskClusters": [],
        "alerts": [],
        "contextualFactors": {
            "stress": "Low",
            "stressScore": 2.8,
            "sleep": "7.8 hrs",
            "sleepQuality": 0.87,
            "activity": "Active",
            "stepCount": 8900,
            "recentTravel": False,
            "caffeineIntake": "Moderate",
            "circadianPhase": "Aligned"
        },
        "passiveSignals": {
            "phoneUsagePattern": "Normal",
            "sleepConsistency": "Consistent",
            "movementPattern": "Healthy",
            "screenTime": "4.1 hrs",
            "lastBackgroundAlert": "None"
        },
        "sensorHistory": [],
        "evidenceTimeline": [
            { "time": "08:30 AM", "event": "Routine rPPG scan completed", "type": "capture" }
        ]
    },
    {
        "id": "P003",
        "name": "Vaibhav Singh",
        "age": 52,
        "gender": "Male",
        "phone": "+91 97654 32109",
        "deviceType": "Samsung Galaxy S24",
        "deviceConnected": True,
        "lastSync": "30 sec ago",
        "riskScore": 85,
        "riskLevel": "Critical",
        "confidence": 0.93,
        "baselineStatus": "Multiple Deviations",
        "anomalyDetected": True,
        "anomalyType": "Multi-System Instability",
        "evidenceGating": "Full Analysis Active",
        "sensorQuality": 0.91,
        "heartRate": 96,
        "hrv": 28,
        "respiratoryRate": 22,
        "consent": { "camera": True, "microphone": True, "wearable": True, "cloudProcessing": True },
        "encryptionStatus": "AES-256 Active",
        "baseline": {
            "shortTerm": { "status": "Critical Deviation", "confidence": 0.94 },
            "midTerm": { "status": "Severe Drift", "confidence": 0.89 },
            "longTerm": { "status": "Abnormal Pattern", "confidence": 0.87 }
        },
        "baselinePhase": "Recalibration Required",
        "rppgData": {
            "lastCapture": "1 min ago",
            "captureQuality": 0.89,
            "lightingScore": 0.87,
            "motionStability": 0.92,
            "signalStrength": "Good",
            "captureCount": 312
        },
        "coughAnalysis": {
            "lastRecording": "3 min ago",
            "audioQuality": 0.91,
            "coughDetected": True,
            "features": {
                "frequency": "Very High",
                "duration": "320ms",
                "intensity": "High",
                "pattern": "Frequent clusters"
            },
            "spectralAnalysis": {
                "mfcc": [0.91, 0.88, 0.94, 0.82],
                "melSpectrogram": "Severe abnormality detected"
            },
            "riskFlags": ["Critical Airway Obstruction", "Severe Inflammation Markers"]
        },
        "diseaseFlags": [
            { "condition": "Severe Respiratory Compromise", "probability": 0.91, "severity": "Critical", "evidence": ["Persistent cough pattern", "Very high respiratory rate"] }
        ],
        "riskClusters": [
            { "category": "Respiratory", "probability": 0.91, "contributing": ["Elevated RR", "Severe cough abnormality"] }
        ],
        "alerts": [
            { "id": "A003", "severity": "Critical", "message": "IMMEDIATE clinician review required", "timestamp": "2 min ago", "status": "Urgent", "requiresAction": True }
        ],
        "contextualFactors": {
            "stress": "Very High",
            "stressScore": 8.9,
            "sleep": "4.1 hrs",
            "sleepQuality": 0.28,
            "activity": "Very Low",
            "stepCount": 1200,
            "recentTravel": False,
            "caffeineIntake": "Very High",
            "circadianPhase": "Severely Misaligned"
        },
        "passiveSignals": {
            "phoneUsagePattern": "Erratic",
            "sleepConsistency": "Severely irregular",
            "movementPattern": "Reduced 75%",
            "screenTime": "11.8 hrs",
            "lastBackgroundAlert": "6 hours ago"
        },
        "sensorHistory": [],
        "evidenceTimeline": [
            { "time": "07:34 AM", "event": "CRITICAL anomaly detected", "type": "detection" },
            { "time": "07:42 AM", "event": "URGENT ALERT - Clinician confirmation REQUIRED", "type": "alert" }
        ]
    }
]