from fastapi import FastAPI
import subprocess
cimport os

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    if not host or '&&' in host or ';' in host:
        return {"status": "error", "message": "Invalid input"}
    safe_host = subprocess.list2cmdline([host])
    result = subprocess.run(['ping', safe_host], capture_output=True, text=True)
    return {"status": "completed", "output": result.stdout}