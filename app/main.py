from fastapi import FastAPI
import subprocess
import shlex

global app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    safe_host = shlex.quote(host)
    subprocess.call(['ping', safe_host])
    return {'status': 'completed'}