from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    # Safe implementation using list instead of shell=True
    if host.strip() and not any(char in host for char in [';', '&', '|', '$']):  # Basic input validation
        subprocess.call(['ping', host])
    return {'status': 'completed'}