from fastapi import FastAPI
import subprocess
def safe_ping(host: str):
    if host in ['127.0.0.1', '::1']:  # Example whitelist of allowed hosts
        subprocess.run(['ping', host], shell=False, capture_output=True, text=True)
    else:
        raise ValueError('Invalid or untrusted host')

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    safe_ping(host)
    return {'status': 'completed'}