from fastapi import FastAPI
import subprocess
from fastapi.encoders import jsonable_encoder

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Secure implementation using subprocess.run with shell=False and a whitelist of allowed hosts
    if host in ['example.com', 'another-example.com']:
        result = subprocess.run(['ping', host], capture_output=True, text=True)
        return jsonable_encoder({"status": "completed", "output": result.stdout})
    else:
        return jsonable_encoder({"status": "error", "message": "Invalid host"})