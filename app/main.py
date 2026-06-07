from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get('/home')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    # Safe implementation
    if host in ['127.0.0.1', '::1']:  # Allow only localhost for demonstration purposes
        subprocess.call(['ping', host], shell=False)
    return {'status': 'completed'}