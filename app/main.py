from fastapi import FastAPI
import subprocess
from shlex import quote
def ping(host: str):
    safe_host = quote(host)
    subprocess.run(f'ping {safe_host}', shell=False)
app = FastAPI()
@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}
@app.get('/ping')
def ping_safe(host: str):
    safe_host = quote(host)
    subprocess.run(f'ping {safe_host}', shell=False)
    return {'status': 'completed'}