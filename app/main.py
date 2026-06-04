from fastapi import FastAPI
import subprocess
from pydantic import BaseModel
def validate_host(host: str) -> bool:
    # Simple validation for demonstration purposes
    return host.startswith('192.168.') or host.startswith('localhost')

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    if validate_host(host):
        try:
            output = subprocess.check_output(['ping', host], stderr=subprocess.STDOUT, timeout=5)
            return {"status": "completed", "output": output.decode('utf-8')}
        except subprocess.CalledProcessError as e:
            return {"status": "failed", "error": e.output.decode('utf-8')}
    else:
        return {"status": "failed", "error": "Invalid host"}