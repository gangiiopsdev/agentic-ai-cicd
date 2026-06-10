from fastapi import FastAPI
import subprocess
import re

def safe_ping(host: str):
    # Validate host to ensure it's a safe domain name or IP address
    if not re.match(r'^[a-zA-Z0-9.-]+$', host):
        return {'status': 'failed', 'error': 'Invalid host'}

app = FastAPI()

@app.get(")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    try:
        output = subprocess.check_output(['ping', re.sub(r'^[a-zA-Z0-9.-]+$', host)], stderr=subprocess.STDOUT, universal_newlines=True)
        return {'status': 'completed', 'output': output}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': e.output}