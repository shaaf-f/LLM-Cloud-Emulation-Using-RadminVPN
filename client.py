import requests
import json

RADMIN_IP = "26.65.113.255"
PORT = "8000"

url = f"http://{RADMIN_IP}:{PORT}/v1/chat/completions"

payload = {
    "model": "qwen2.5-coder:7b",
    "messages": [
        {
            "role": "user",
            "content": "Say hello in one sentence."
        }
    ],
    "temperature": 0.0,
    "stream": False
}

response = requests.post(url, json=payload, timeout=120)

print("Status:", response.status_code)

try:
    data = response.json()
except Exception:
    print("Raw response:")
    print(response.text)
    raise SystemExit

if response.status_code != 200:
    print("Server error:")
    print(json.dumps(data, indent=2))
    raise SystemExit

print(data["choices"][0]["message"]["content"])