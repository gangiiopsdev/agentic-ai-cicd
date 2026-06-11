from fastapi import FastAPI
import subprocess

app = FastAPI()

def safe_ping(host: str):
    # Secure implementation
    subprocess.run(['/usr/bin/ping', host], capture_output=True, text=True)

@app.get('/ping')
def ping(host: str):
    return safe_ping(host)

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}