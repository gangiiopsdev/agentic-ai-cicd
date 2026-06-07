from fastapi import FastAPI
import subprocess
import re

app = FastAPI()

def safe_ping(host):
    # Improved validation using regex
    if not re.match(r'^[a-zA-Z0-9.-]+$', host):
        return {'error': 'Invalid host input'}
    try:
        output = subprocess.check_output(['ping', host], stderr=subprocess.STDOUT, universal_newlines=True)
        return output
    except subprocess.CalledProcessError as e:
        return str(e.output)

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    return safe_ping(host)