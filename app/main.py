from fastapi import FastAPI
import subprocess
import re

app = FastAPI()

global host_validator
host_validator = re.compile(r'^[a-zA-Z0-9.-]+$')

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    if not host_validator.match(host):
        return {"status": "failed", "error": "Invalid hostname"}
    try:
        result = subprocess.run(['ping', host], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return {"status": "completed", "stdout": result.stdout.decode('utf-8')}
    except subprocess.CalledProcessError as e:
        return {"status": "failed", "stderr": e.stderr.decode('utf-8')}