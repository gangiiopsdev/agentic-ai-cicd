from fastapi import FastAPI
import subprocess
from pydantic import BaseModel
def safe_ping(host):
    allowed_hosts = ['example.com', '192.168.1.1']  # Define a list of allowed hosts
    if host not in allowed_hosts:
        raise ValueError('Host is not allowed')
class PingRequest(BaseModel):
    host: str
app = FastAPI()
@app.get("/home")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}
@app.post("/ping")
def ping(request: PingRequest): 
    try:
        output = subprocess.run(['ping', '-c 1', request.host], capture_output=True, text=True, check=True)
        return {"status": "completed", "output": output.stdout}
    except subprocess.CalledProcessError as e:
        return {"status": "failed", "error": e.stderr}