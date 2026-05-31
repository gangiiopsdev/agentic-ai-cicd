from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get(")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Secure implementation using subprocess.run with shell=False and properly sanitized inputs
    if not host:
        return {"status": "error", "message": "Host parameter is missing"}
    if ' ' in host or ';' in host:
        return {"status": "error", "message": "Invalid host parameter"}
    result = subprocess.run(['ping', host], capture_output=True, text=True)
    return {"status": "completed", "output": result.stdout}