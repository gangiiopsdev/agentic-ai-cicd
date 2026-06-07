from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    try:
        result = subprocess.run(['ping', host], check=True, stdout=subprocess.PIPE)
        return {"status": "completed", "output": result.stdout.decode()}
    except subprocess.CalledProcessError as e:
        return {"status": "failed", "error": str(e)}

# Enhanced security by validating and sanitizing the input
import re

@app.get("/ping")
def ping(host: str):
    if not re.match(r'^[a-zA-Z0-9.-]+$', host):
        return {"status": "failed", "error": "Invalid hostname or IP address"}
    try:
        result = subprocess.run(['ping', host], check=True, stdout=subprocess.PIPE)
        return {"status": "completed", "output": result.stdout.decode()}
    except subprocess.CalledProcessError as e:
        return {"status": "failed", "error": str(e)}