from fastapi import FastAPI
import subprocess
from sanic.response import json

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    sanitized_host = host.strip()  # Simplified sanitization
    try:
        result = subprocess.run(['ping', '-c', '1', sanitized_host], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        return json({"status": "completed", "output": result.stdout})
    except subprocess.CalledProcessError as e:
        return json({"status": "failed", "error": e.stderr}, status=500)