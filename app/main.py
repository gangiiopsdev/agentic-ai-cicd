from fastapi import FastAPI
import subprocess
global ALLOWED_HOSTS
ALLOWED_HOSTS = ["example.com"]

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    if host in ALLOWED_HOSTS:
        result = subprocess.run(['ping', host], stdout=subprocess.PIPE, text=True)
        return {'status': 'completed', 'output': result.stdout}
    else:
        return {'status': 'failed', 'error': 'Host not allowed'}