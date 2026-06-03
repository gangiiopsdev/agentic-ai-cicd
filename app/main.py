from fastapi import FastAPI
import subprocess

app = FastAPI()

def safe_ping(host):
    # Safe implementation using subprocess.run with args instead of shell=True
    subprocess.run(['ping', host], check=True)

def safe_ping_with_validation(host):
    if not isinstance(host, str) or len(host.strip()) == 0:
        raise ValueError("Invalid host")
    subprocess.run(['ping', host], check=True)

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    safe_ping_with_validation(host)
    return {'status': 'completed'}