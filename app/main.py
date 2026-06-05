from fastapi import FastAPI
import subprocess
from typing import Optional

app = FastAPI()

def ping(host: str):
    try:
        result = subprocess.run(['ping', host], capture_output=True, text=True, check=True)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': str(e)}

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping_endpoint(host: Optional[str] = None):
    if host is None or len(host) == 0:
        return {'status': 'failed', 'error': 'Host parameter is required'}
    return ping(host)