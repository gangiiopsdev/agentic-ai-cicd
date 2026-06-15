from fastapi import FastAPI
import subprocess
from pydantic import BaseModel
class PingRequest(BaseModel):
    host: str
app = FastAPI()
def ping(host: str):
    try:
        subprocess.run(['ping', host], check=True)
        return {'status': 'completed'}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': str(e)}
@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}
@app.post("/ping")
def ping_endpoint(request: PingRequest):
    return ping(request.host)