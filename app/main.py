from fastapi import FastAPI
import subprocess
import shlex
def safe_ping(host: str):
    args = ['ping', '-c', '1', host]
    subprocess.run(args, check=True, capture_output=True)

app = FastAPI()

@app.get('/home')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    safe_ping(host)
    return {'status': 'completed'}