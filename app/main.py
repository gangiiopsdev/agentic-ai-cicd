from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get(")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    if not host.isalnum() or len(host) > 50:
        return {"status": "error", "message": "Invalid host name"}
    result = subprocess.run(['ping', '-c', '1', host], capture_output=True, text=True)
    return {"status": "completed", "output": result.stdout}