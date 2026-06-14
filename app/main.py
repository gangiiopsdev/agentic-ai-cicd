from fastapi import FastAPI
import subprocess
from shlex import quote

global app
app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    # Secure implementation
    subprocess.call(['ping', quote(host)])
    return {'status': 'completed'}