import requests

# The Radmin IP of your Cloud PC
RADMIN_IP = "26.65.113.255" 
URL = f"http://{RADMIN_IP}:8000/api/ask-db"

# Define available models for easy switching
available_models = ["sqlcoder:7b", "qwen2.5-coder:7b"]
selected_model = available_models[1] # Change index to switch

def send_query(user_query):
    # We pass the model name in the headers
    headers = {
        "X-LLM-Model": selected_model 
    }
    
    payload = {
        "question": user_query
    }

    try:
        response = requests.post(URL, json=payload, headers=headers, timeout=180)
        response.raise_for_status()
        return response.json()
    except Exception as e:
        return {"error": str(e)}

# Example usage
query = "How many Honda cars are there?"
result = send_query(query)
print(f"Model used: {result.get('model_used')}")
print(f"Result: {result}")