from fastapi import FastAPI
import subprocess
import shlex
def safe_ping(host: str):
    args = ['ping', '-c', '1', host]  # Use known options to reduce command injection risk
    return subprocess.call(args, shell=False)

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    result = safe_ping(host)
    return {'status': 'completed', 'result': result}