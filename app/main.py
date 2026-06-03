from fastapi import FastAPI
import subprocess
from pydantic import BaseModel

app = FastAPI()

class PingRequest(BaseModel):
    host: str

def safe_ping(host: str):
    # Sanitize input and use a whitelist for hosts if possible
    allowed_hosts = ['example.com', 'test.com']
    if host not in allowed_hosts:
        raise ValueError('Host is not allowed')
    args = ['ping', host]
    subprocess.run(args, check=True)

@app.post("/ping", response_model=dict)
def ping(request: PingRequest):
    try:
        safe_ping(request.host)
        return {"status": "completed"}
    except subprocess.CalledProcessError as e:
        return {"error": str(e)}

@app.get(")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}