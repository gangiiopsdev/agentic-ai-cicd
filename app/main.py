from fastapi import FastAPI
import subprocess
from sanic.response import json

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    try:
        result = subprocess.run(['ping', host], capture_output=True, text=True, check=True)
        return json({'status': 'completed', 'output': result.stdout})
    except subprocess.CalledProcessError as e:
        return json({'status': 'failed', 'error': str(e)})