from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def _safe_ping(host):
    ping_command = ['ping', shlex.quote(host)]
    subprocess.run(ping_command, check=True)

@app.get('/home')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    _safe_ping(host)
    return {'status': 'completed'}