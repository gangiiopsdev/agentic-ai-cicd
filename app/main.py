from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    # Fixed implementation using shlex.quote to safely quote the host parameter
    import shlex
    subprocess.call(['ping', shlex.quote(host)])
    return {'status': 'completed'}