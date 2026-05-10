from fastapi import FastAPI
from pydantic import BaseModel
import uvicorn

app = FastAPI()

class TestRequest(BaseModel):
    query: str

@app.post("/test-connection")
def handle_query(request: TestRequest):
    print(f"\n[RECEIVED] Query from interface: '{request.query}'")
    
    # Simulate processing the query
    response_message = f"Cloud PC successfully processed: '{request.query}'"
    
    return {"status": "ok", "reply": response_message}

if __name__ == "__main__":
    print("Starting Test Server on port 8000...")
    # host="0.0.0.0" is required to allow connections from the Radmin network
    uvicorn.run(app, host="0.0.0.0", port=8000)