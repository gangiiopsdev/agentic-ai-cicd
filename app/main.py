from fastapi import FastAPI
import subprocess
import re

def safe_ping(host):
    if not re.match(r'^[a-zA-Z0-9.-]+$', host):
        return 'Invalid host'
    try:
        result = subprocess.run(['ping', '-c', '4', host], capture_output=True, text=True)
        return result.stdout
    except Exception as e:
        return str(e)

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    response = safe_ping(host)
    return {"status": "completed", "response": response}