import requests

# Your Radmin IP
RADMIN_IP = "26.65.113.255" 
PORT = "8000"
URL = f"http://{RADMIN_IP}:{PORT}/api/chat"

# The model you want to test
MODEL = "qwen2.5-coder:7b"

print("======================================================")
print(f" LLM Terminal -> Connected to {RADMIN_IP}")
print(f" Using Model: {MODEL}")
print("======================================================")

while True:
    user_query = input("\nYou: ")
    
    if user_query.strip().lower() == 'exit':
        print("Closing connection...")
        break
        
    if not user_query.strip():
        continue

    print("Thinking...")
    try:
        # Send the prompt and model choice to your Cloud PC
        payload = {
            "prompt": user_query,
            "model": MODEL
        }
        
        response = requests.post(URL, json=payload, timeout=120)
        response.raise_for_status() 
        
        # Print the LLM's reply
        data = response.json()
        print(f"\n{MODEL}: {data['reply']}")
            
    except requests.exceptions.ConnectionError:
        print("\n[ERROR] Connection refused! Is the server running and is Port 8000 open in the Firewall?")
    except requests.exceptions.HTTPError as e:
        print(f"\n[SERVER ERROR]: {e.response.text}")
    except Exception as e:
        print(f"\n[ERROR] Something went wrong: {e}")