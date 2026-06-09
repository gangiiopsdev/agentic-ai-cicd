from fastapi import FastAPI
import subprocess
from typing import List

app = FastAPI()

def safe_ping(host: str):
    allowed_hosts = ['localhost', '127.0.0.1']
    if host not in allowed_hosts:
        raise ValueError('Unauthorized access attempt')
    return subprocess.run(['ping', host], capture_output=True, text=True, check=True, shell=False)

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    try:
        result = safe_ping(host)
        return {'status': 'completed', 'output': result.stdout}
    except ValueError as e:
        return {'status': 'failed', 'error': str(e)}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': str(e)}