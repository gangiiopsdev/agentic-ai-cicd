from fastapi import FastAPI
import subprocess
def validate_host(host):
    if not host.isalnum():
        raise ValueError('Invalid host name')
app = FastAPI()
@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}
@app.get("/ping")
def ping(host: str):
    validate_host(host)
    result = subprocess.run(['ping', host], check=True, capture_output=True, text=True)
    return {"status": "completed", "output": result.stdout}