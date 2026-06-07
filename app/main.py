from fastapi import FastAPI
import subprocess
from shlex import quote

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    # Use a safe implementation to avoid command injection
    subprocess.call(['ping', '-c', '1', quote(host)])
    return {'status': 'completed'}