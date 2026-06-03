from fastapi import FastAPI
import subprocess
import re

def _validate_ip(ip):
    return re.match(r'^[0-9]{1,3}\.[0-9]{1,3}\. [0-9]{1,3}\. [0-9]{1,3}$', ip) is not None

def _run_ping(host):
    try:
        result = subprocess.run(['ping', host], capture_output=True, text=True)
        return {'status': 'completed', 'output': result.stdout}
    except Exception as e:
        return {'status': 'error', 'message': str(e)}

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    if _validate_ip(host):
        return _run_ping(host)
    else:
        return {'status': 'invalid_host'}