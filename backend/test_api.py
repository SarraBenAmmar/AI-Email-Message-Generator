# test_api_complete.py
import requests
import json
import time

BASE_URL = "http://localhost:8000"

def test_all_endpoints():
    # Test health endpoint
    response = requests.get(f"{BASE_URL}/health")
    print(f"✅ Health check: {response.status_code} - {response.json()}")
    
    # Test channels endpoint
    response = requests.get(f"{BASE_URL}/api/v1/channels")
    print(f"✅ Channels: {response.status_code} - {response.json()}")
    
    # Test generate endpoint with detailed payload
    payload = {
        "prompt": "digital marketing strategies for small businesses",
        "tone": "professional",
        "audience": "prospect", 
        "sequence_length": 3,
        "channel": "email"
    }
    
    print(f"\n🚀 Testing generate endpoint with: {json.dumps(payload, indent=2)}")
    
    response = requests.post(f"{BASE_URL}/api/v1/generate", json=payload)
    print(f"📨 Generate endpoint status: {response.status_code}")
    
    if response.status_code == 200:
        result = response.json()
        print(f"✅ SUCCESS! Generated {len(result.get('sequence', []))} items")
        print(f"📊 Metadata: {result.get('metadata', {})}")
        
        # Show the generated content
        for item in result.get('sequence', []):
            print(f"\n--- Step {item['step']}: {item['purpose']} ---")
            print(f"Subject: {item['subject']}")
            print(f"Body: {item['body'][:100]}...")
            
    elif response.status_code == 404:
        print("❌ ERROR: Generate endpoint not found (404)")
        print("   Make sure your router is properly mounted")
    elif response.status_code == 422:
        print("❌ ERROR: Validation error (422)")
        print(f"   Response: {response.text}")
    else:
        print(f"❌ ERROR: Unexpected status code {response.status_code}")
        print(f"   Response: {response.text}")

if __name__ == "__main__":
    test_all_endpoints()