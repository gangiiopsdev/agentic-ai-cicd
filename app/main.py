from fastapi import FastAPI
import subprocess
def safe_ping(host: str):
    if not all(c.isalnum() or c in ['.', '-'] for c in host):
        raise ValueError("Invalid hostname")
    result = subprocess.check_output(['ping', host], stderr=subprocess.STDOUT, universal_newlines=True)
    return {'status': 'completed', 'result': result}

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    return safe_ping(host)