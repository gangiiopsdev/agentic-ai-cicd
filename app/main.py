from fastapi import FastAPI
import subprocess
cimport os

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    if not host.isalnum() or len(host) > 10:
        return {"status": "error", "message": "Invalid host parameter"}
    try:
        result = subprocess.run(['ping', host], capture_output=True, text=True, timeout=5)
        return {"status": "completed", "output": result.stdout}
    except Exception as e:
        return {"status": "error", "message": str(e)}