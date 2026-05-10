from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import requests
import uvicorn

app = FastAPI(title="Pure LLM Bridge")

# Define what the incoming request looks like
class ChatRequest(BaseModel):
    prompt: str
    model: str = "qwen2.5-coder:7b" # Default model

@app.post("/api/chat")
def chat_with_llm(request: ChatRequest):
    print(f"\n[RECEIVED] Prompt: '{request.prompt}'")
    print(f"[FORWARDING] Sending to Ollama ({request.model})...")
    
    ollama_url = "http://localhost:11434/v1/chat/completions"
    
    payload = {
        "model": request.model,
        "messages": [{"role": "user", "content": request.prompt}],
        "temperature": 0.7
    }
    
    try:
        # Talk to Ollama locally on the Cloud PC
        llm_response = requests.post(ollama_url, json=payload, timeout=120)
        llm_response.raise_for_status()
        
        # Extract the text from Ollama's response
        reply_text = llm_response.json()["choices"][0]["message"]["content"]
        
        print("[SUCCESS] Sending response back to interface.")
        return {"reply": reply_text}
        
    except requests.exceptions.ConnectionError:
        print("[ERROR] Could not reach Ollama. Is it running?")
        raise HTTPException(status_code=502, detail="Ollama is not running on the Cloud PC.")
    except Exception as e:
        print(f"[ERROR] {str(e)}")
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    print("Starting LLM Bridge Server on port 8000...")
    # host="0.0.0.0" allows the Radmin VPN traffic to hit this server
    uvicorn.run(app, host="0.0.0.0", port=8000)