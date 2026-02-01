# GUVI Hackathon: Problem Statement 01 Summary

## 🎯 Core Objective
Build a secure REST API that detects whether a given voice sample is **AI-generated** or **Human** across five supported languages.

---

## 🌐 Supported Languages
-   **Tamil**
-   **English**
-   **Hindi**
-   **Malayalam**
-   **Telugu**

---

## ⚙️ Technical Specifications
-   **Endpoint**: `POST /api/voice-detection`
-   **Input Format**: JSON with Base64-encoded MP3 audio.
-   **Required Header**: `x-api-key: YOUR_SECRET_API_KEY`
-   **Request Body**:
    ```json
    {
      "language": "Tamil",
      "audioFormat": "mp3",
      "audioBase64": "..."
    }
    ```

---

## 📋 Mandatory Response Format
```json
{
  "status": "success",
  "language": "Tamil",
  "classification": "AI_GENERATED",
  "confidenceScore": 0.94,
  "explanation": "..."
}
```

---

## 🏆 Evaluation & Rules
*   **Accuracy**: Detection precision across all languages.
*   **Explanation Quality**: The **"Winning Edge"**—technical reasoning is required.
*   **No Hard-coding**: Dynamic analysis is mandatory (Strictly Prohibited).
*   **Local Logic**: Focus on built-in models/logic rather than external restricted APIs.

---

## 🧠 Our Approach (AVIS System)
1.  **Hybrid Engine**: Combines **Wav2Vec2** Transformer models with **Acoustic Feature Extraction** (Pitch, Spectral Centroid, ZCR).
2.  **Robustness**: Built-in **Noise Reduction** and **Peak Normalization** for real-world audio quality.
3.  **Explainable AI (XAI)**: Maps neural artifacts to human-readable scientific reasons.
4.  **Performance**: Features a **Startup Warm-up** routine for zero-latency during jury evaluation.

---

## 📂 Project Files
*   `app.py`: API Server & Security
*   `detect.py`: AI Engine & Acoustic Analysis
*   `test_locally.py`: Local Verification Script
*   `README.md`: Full Documentation & Diagrams
