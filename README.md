# AudioShield AI: Voice Fraud Detection System

> **Problem Statement 01**: AI-Generated Voice Detection for Regional Languages

![Architecture](Architechture.png)

## 🚀 Overview
**AudioShield AI** is a high-performance REST API designed to detect AI-generated voice deepfakes with exceptional accuracy. Built for the **GUVI Hackathon**, it specifically addresses the challenge of identifying synthetic audio in **Tamil, English, Hindi, Malayalam, and Telugu**.

Unlike standard detectors, AudioShield uses a **Multi-Model Voting Ensemble** approach, aggregating the intelligence of 4 state-of-the-art Wav2Vec2 models to make a final, highly reliable decision.

## 🎯 Problem It Solves
With the rise of Generative AI, voice scams and deepfakes are becoming indistinguishable from reality. Financial fraud, impersonation, and misinformation are growing threats. AudioShield provides a robust, scalable defense mechanism that can be integrated into calls, messaging apps, and verification systems.

## ✨ Key Features
*   **🛡️ Voting Ensemble Power**: Leverages 4 distinct AI models (MelodyMachine, Mo-Creator, Hemgg, Gustking-XLSR) to minimize false positives.
*   **🌍 Multi-Lingual Support**: Optimized for Indian regional languages (Tamil, Telugu, Hindi, Malayalam) + English.
*   **⚡ Zero Cold Start**: Implements a "Warm-up" routine to ensure the first API request is as fast as the 100th.
*   **🚀 Render-Ready**: Configured for seamless deployment on cloud platforms like Render.
*   **🔍 Explainable AI**: Provides detailed JSON responses with classification confidence and logic.

## 🏗️ System Architecture
The system follows a **Microservices-ready, Layered Architecture**:

```mermaid
graph TD
    User[Client / Postman] -->|HTTP POST (Base64)| API[FastAPI Service]
    API -->|Async Thread| Engine[Detection Engine]
    
    subgraph "Ensemble Committee (The AI Core)"
        Engine -->|Input| M1[MelodyMachine]
        Engine -->|Input| M2[Mo-Creator]
        Engine -->|Input| M3[Hemgg]
        Engine -->|Input| M4[Gustking (XLSR)]
        
        M1 -->|Vote| Agg[Weighted Aggregator]
        M2 -->|Vote| Agg
        M3 -->|Vote| Agg
        M4 -->|Vote| Agg
    end
    
    Agg -->|Final Score| Verdict[Classification Logic]
    Verdict -->|JSON Response| User
```

### Core Components
1.  **FastAPI Layer (`main.py`)**: Handles HTTP requests, validation, and async processing.
2.  **Detection Engine (`detect.py`)**: Manages model loading, inference, and the ensemble voting logic.
3.  **Models**:
    *   `MelodyMachine/Deepfake-audio-detection-V2`
    *   `mo-thecreator/Deepfake-audio-detection`
    *   `Hemgg/Deepfake-audio-detection`
    *   `Gustking/wav2vec2-large-xlsr-deepfake-audio-classification` (The "Expert" model)

## 🛠️ Tech Stack
*   **Language**: Python 3.10+
*   **API Framework**: FastAPI, Uvicorn
*   **ML Libraries**: PyTorch, Transformers, Librosa, NumPy
*   **Deployment**: Docker-ready, Render-compatible

## 🚀 Installation & Usage

### 1. Clone the Repository
```bash
git clone https://github.com/krish1440/AI-Generated-Voice-Detection.git
cd AI-Generated-Voice-Detection
```

### 2. Install Dependencies
```bash
pip install -r requirements.txt
```

### 3. Run the Server
```bash
python main.py
```
*The server will start on port `8000` (or the PORT env var).*
*Note: On the first run, it will download necessary model weights (approx. 2-3GB).*

## 🔌 API Documentation

### Detect Voice
**Endpoint**: `POST /api/voice-detection`

**Request Body** (JSON):
```json
{
  "language": "Tamil",
  "audioFormat": "mp3",
  "audioBase64": "<Base64 encoded MP3 string>"
}
```

**Response** (Success):
```json
{
  "status": "success",
  "language": "Tamil",
  "classification": "AI_GENERATED",
  "confidenceScore": 0.98,
  "explanation": "Ensemble Analysis: 4/4 models flagged this audio as AI-generated."
}
```

**Response** (Error):
```json
{
  "status": "error",
  "message": "Invalid Base64 encoding."
}
```

## ☁️ Deployment (Render)
This project is configured for Render.
1.  Create a new **Web Service** on Render.
2.  Connect your GitHub repository.
3.  **Build Command**: `pip install -r requirements.txt`
4.  **Start Command**: `python main.py`
5.  Set Environment Variables (Optional): `PORT` (Render sets this automatically).

---
*Developed for GUVI Hackathon.*
