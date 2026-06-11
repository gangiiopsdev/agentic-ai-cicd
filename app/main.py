from fastapi import FastAPI
import subprocess
from shlex import quote
def ping(host: str):
    safe_host = quote(host)
    subprocess.run(['ping', '-c', '1', safe_host], check=True)
app = FastAPI()
@app.get('/home')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}
@app.get('/ping_safe')
def ping_safe(host: str):
    safe_host = quote(host)
    subprocess.run(['ping', '-c', '1', safe_host], check=True)
    return {'status': 'completed'}