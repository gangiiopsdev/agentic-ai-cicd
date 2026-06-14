from fastapi import FastAPI
import subprocess
import re

app = FastAPI()

def validate_host(host):
    return re.match(r'^[a-zA-Z0-9.-]+$', host) is not None

@app.get("/ping")
def ping(host: str):
    if not validate_host(host):
        return {"status": "error", "output": "Invalid host"}
    try:
        result = subprocess.run(["ping", host], check=True, capture_output=True, text=True)
        return {"status": "completed", "output": result.stdout}
    except subprocess.CalledProcessError as e:
        return {"status": "error", "output": str(e)}

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}