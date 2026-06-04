from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    # Sanitize input to avoid injection attacks
    safe_host = subprocess.list2cmdline([host])
    args = ['ping', safe_host]
    subprocess.call(args)
    return {'status': 'completed'}