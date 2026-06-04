from fastapi import FastAPI
import subprocess
from shlex import quote

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    # Secure implementation using shlex.quote and shell=False
    subprocess.call(['ping', quote(host)], shell=False)
    return {'status': 'completed'}