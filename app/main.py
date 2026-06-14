from fastapi import FastAPI
import subprocess
global allowlist = ['google.com', '127.0.0.1']

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    if host in allowlist:
        subprocess.run(['ping', host], check=True, capture_output=True, text=True)
    else:
        return {'status': 'error', 'message': 'Host not allowed'}

    return {'status': 'completed'}