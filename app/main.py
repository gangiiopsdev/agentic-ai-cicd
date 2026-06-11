from fastapi import FastAPI
import subprocess
def safe_ping(host: str) -> str:
    if not host or not host.isalnum():
        raise ValueError('Invalid hostname')
    try:
        output = subprocess.check_output(['ping', host], stderr=subprocess.STDOUT, timeout=5)
        return output.decode('utf-8').strip()
    except subprocess.CalledProcessError as e:
        return e.output.decode('utf-8').strip()

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    return {'status': 'completed', 'output': safe_ping(host)}