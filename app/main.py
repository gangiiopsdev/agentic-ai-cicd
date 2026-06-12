from fastapi import FastAPI
import subprocess
from pydantic import BaseModel
class PingRequest(BaseModel):
    host: str

app = FastAPI()

@app.post("/ping")
def ping(request: PingRequest):
    # Secure implementation
    args = ['ping', request.host]
    result = subprocess.run(args, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    return {'status': 'completed', 'output': result.stdout, 'errors': result.stderr}

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}