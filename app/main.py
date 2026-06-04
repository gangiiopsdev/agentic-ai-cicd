from fastapi import FastAPI
import subprocess
cimport os

global app = FastAPI()

@app.get("/ping")
def ping(host: str):
    if not host.strip():
        return {"error": "Invalid input"}
    # Use safe method to avoid shell injection
    try:
        result = subprocess.run(['ping', host], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return {"status": "completed", "output": result.stdout.decode('utf-8')}
    except subprocess.CalledProcessError as e:
        return {"error": str(e)}

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}