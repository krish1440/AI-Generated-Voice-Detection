# AudioShield AI: Project Architecture & Documentation

## 1. Project Overview
**AudioShield AI** is a specialized REST API designed to detect AI-generated voice deepfakes across 5 Indian languages (Tamil, English, Hindi, Malayalam, Telugu). It was built to solve the challenge of distinguishing between human computation and synthetic media with high accuracy, adhering to strict hackathon requirements.

## 2. System Architecture

The system follows a **Microservices-ready, Layered Architecture**:

```mermaid
graph TD
    User[Client / Postman] -->|HTTP POST (Base64)| API[FastAPI Service (main.py)]
    API -->|Async Thread| Engine[Detection Engine (detect.py)]
    
    subgraph "Ensemble Committee (The AI Core)"
        Engine -->|Input| M1[MelodyMachine (Generic)]
        Engine -->|Input| M2[Mo-Creator (Fine-Tuned)]
        Engine -->|Input| M3[Hemgg (Diverse Data)]
        Engine -->|Input| M4[Gustking (XLSR - 1GB)]
        
        M1 -->|Vote| Agg[Weighted Aggregator]
        M2 -->|Vote| Agg
        M3 -->|Vote| Agg
        M4 -->|Vote| Agg
    end
    
    Agg -->|Final Score| Verdict[Classification Logic]
    Verdict -->|JSON Response| User
```

### 2.1 Core Components

#### **A. The API Layer (`main.py`)**
-   **Framework**: FastAPI (High-performance, async).
-   **Protocol**: REST over HTTP.
-   **Security**: Public Access (API Key validation removed for hackathon demo).
-   **Lifecycle Management**: Uses `lifespan` to pre-load heavy AI models during server startup (Zero Cold Start).
-   **Concurrency**: Implements `run_in_threadpool` to prevent the heavy AI inference from blocking other API requests.

#### **B. The Detection Engine (`detect.py`)**
-   **Ensemble Strategy**: Instead of relying on one model, we use a **Weighted Voting Ensemble** of 4 State-of-the-Art models.
-   **Diversity**:
    -   3x `Wav2Vec2-Base` models fine-tuned on different datasets.
    -   1x `Wav2Vec2-Large-XLSR` (1.2GB) for robust cross-lingual feature extraction.
-   **Logic**:
    1.  Audio is decoded from Base64 and resampled to 16kHz.
    2.  All 4 models run inference in parallel/sequence.
    3.  Votes are weighted (XLSR gets higher weight due to size).
    4.  **Threshold**: > 0.5 Score triggers `AI_GENERATED`.

### 2.2 Models Used
1.  **MelodyMachine/Deepfake-audio-detection-V2**: General purpose detector.
2.  **mo-thecreator/Deepfake-audio-detection**: Reliable baseline.
3.  **Hemgg/Deepfake-audio-detection**: Adds diversity in training data.
4.  **Gustking/wav2vec2-large-xlsr-deepfake-audio-classification**: The "Heavyweight" expert for complex cases.

## 3. API Specification

**Endpoint**: `POST /api/voice-detection`

**Headers**:
-   `x-api-key`: `v_secret_key_123`
-   `Content-Type`: `application/json`

**Request Body**:
```json
{
  "language": "Tamil",
  "audioFormat": "mp3",
  "audioBase64": "SUQzBAAAAAAAI1..."
}
```

**Response Body**:
```json
{
  "status": "success",
  "language": "Tamil",
  "classification": "AI_GENERATED",
  "confidenceScore": 0.98,
  "explanation": "Ensemble Analysis: 4/4 models flagged this audio as AI-generated."
}
```

## 4. Performance & Reliability
-   **Accuracy**: Achieved **~91.4%** on the validation dataset (70+ files).
-   **Latency**: First request is instant (due to warmup).
-   **Scalability**: The non-blocking architecture allows the API to handle concurrent requests without freezing.

## 5. File Structure
-   `main.py`: The entry point for the API server.
-   `detect.py`: Contains the `AudioDetector` class and ensemble logic.
-   `test_api_strict.py`: Verification script to test strict adherence to specs.
-   `.env`: Configuration secrets.
-   `audio/`: Dataset for testing.
