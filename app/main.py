from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    allowed_hosts = ['localhost', '127.0.0.1']
    if host not in allowed_hosts:
        return {'status': 'failed', 'error': 'Host is not allowed'}
    try:
        output = subprocess.check_output(['ping', host], stderr=subprocess.STDOUT, timeout=10)
        return {'status': 'completed', 'output': output.decode()}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': str(e.output)}

@app.get("/")
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}