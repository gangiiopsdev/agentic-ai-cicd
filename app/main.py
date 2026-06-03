from fastapi import FastAPI
import subprocess
import shlex
def run_ping(host):
    safe_host = shlex.quote(host)
    subprocess.call(['ping', safe_host])

app = FastAPI()

@app.get('/home')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    run_ping(host)
    return {'status': 'completed'}