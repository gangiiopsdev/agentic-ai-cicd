from fastapi import FastAPI
import subprocess
import re

app = FastAPI()

@app.get("/home")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Validate the input to allow only alphanumeric characters and periods
    if not re.match(r'^[a-zA-Z0-9.]+$', host):
        return {'status': 'failed', 'error': 'Invalid host name'}
    try:
        output = subprocess.check_output(['ping', host], stderr=subprocess.STDOUT, timeout=10)
        return {'status': 'completed', 'output': output.decode()}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': e.output.decode()}