from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    # Fixed implementation with shell=False and using shlex.quote for safe input handling
    import shlex
    safe_host = shlex.quote(host)
    subprocess.call(['ping', safe_host], shell=False)
    return {'status': 'completed'}