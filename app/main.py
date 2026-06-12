from fastapi import FastAPI
import subprocess
import re

app = FastAPI()

@app.get("")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Input validation
    if not re.match(r'^[a-zA-Z0-9.-]{1,255}$', host):
        raise ValueError('Invalid hostname')
    try:
        result = subprocess.run(['ping', '-c', '4', host], capture_output=True, text=True, check=True, shell=False)
        return {"status": "completed", "output": result.stdout}
    except subprocess.CalledProcessError as e:
        return {"status": "failed", "error": e.stderr}