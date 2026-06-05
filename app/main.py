from fastapi import FastAPI
import subprocess
import re

app = FastAPI()

@app.get('/')
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get('/ping')
def ping(host: str):
    # Validate the input to ensure it does not contain malicious characters
    if not re.match(r'^[a-zA-Z0-9-.]+$', host):  # Basic regex to allow alphanumeric and common symbols
        return {"status": "error", "message": "Invalid hostname"}
    result = subprocess.run(['ping', host], capture_output=True, text=True)
    return {"status": "completed", "output": result.stdout}