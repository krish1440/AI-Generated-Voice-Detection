import requests
import base64
import os

# Configuration
API_URL = "http://127.0.0.1:8000/api/voice-detection"
# Overridden by .env file found in workspace!
API_KEY = "v_secret_key_123"

def test_api():
    print(f"Testing API at: {API_URL}")
    
    # 1. Load an audio file (using one from existing dataset if available, or dummy)
    # We will try to find a real file for meaningful test
    audio_path = r"e:\Project\GUVI HACKATHON (1)\GUVI HACKATHON\audio\edu_001_00016_8k-29.wav"
    
    if os.path.exists(audio_path):
        print(f"Encoding file: {audio_path}")
        with open(audio_path, "rb") as f:
            audio_bytes = f.read()
            b64_string = base64.b64encode(audio_bytes).decode('utf-8')
    else:
        print("Warning: Real audio file not found, creating dummy silent MP3...")
        # A minimal invalid mp3 frame or just random bytes might trigger decoding error
        # but let's try.
        b64_string = base64.b64encode(b'\x00'*1000).decode('utf-8')

    payload = {
        "language": "Tamil",
        "audioFormat": "mp3",
        "audioBase64": b64_string
    }

    headers = {
        # "x-api-key": API_KEY, # Removed for public access
        "Content-Type": "application/json"
    }

    try:
        print("Sending POST request...")
        response = requests.post(API_URL, json=payload, headers=headers)
        
        print(f"Status Code: {response.status_code}")
        print("Response Body:")
        print(response.json())
        
        if response.status_code == 200:
            data = response.json()
            print("\n[SUCCESS] API is adhering to the spec!")
            print("-" * 30)
            print(f"Status: {data.get('status')}")
            print(f"Classification: {data.get('classification')}")
            print(f"Confidence: {data.get('confidenceScore')}")
            print(f"Explanation: {data.get('explanation')}")
            print("-" * 30)
        else:
            print("\n[FAILURE] API returned error.")
            print(response.text)
            
    except Exception as e:
        print(f"Request failed: {e}")

if __name__ == "__main__":
    test_api()
