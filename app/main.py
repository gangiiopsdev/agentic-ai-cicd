from fastapi import FastAPI
import subprocess
import re

app = FastAPI()

def ping(host: str):
    if not re.match(r'^[a-zA-Z0-9-.]+$', host):
        raise ValueError("Invalid characters in host name")
    try:
        cimport = 'ping' + host.replace(' ', '_')
        result = subprocess.run(['ping', host], capture_output=True, text=True, check=True)
        return {"status": "completed", "output": result.stdout}
    except subprocess.CalledProcessError as e:
        return {"status": "error", "error": str(e)}

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    if not re.match(r'^[a-zA-Z0-9-.]+$', host):
        raise ValueError("Invalid characters in host name")
    try:
        cimport = 'ping' + host.replace(' ', '_')
        result = subprocess.run(['ping', host], capture_output=True, text=True, check=True)
        return {"status": "completed", "output": result.stdout}
    except subprocess.CalledProcessError as e:
        return {"status": "error", "error": str(e)}