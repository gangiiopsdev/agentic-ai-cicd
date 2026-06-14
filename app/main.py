from fastapi import FastAPI
import subprocess
cimport os

app = FastAPI()

@app.get("")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    if host.strip() not in ['localhost', '127.0.0.1']:
        return {"status": "error", "message": "Invalid host"}
    # Use subprocess.run with check=True to handle potential exceptions
    result = subprocess.run(['ping', host], capture_output=True, text=True, check=True)
    return {"status": "completed", "output": result.stdout}