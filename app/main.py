from fastapi import FastAPI
import subprocess

def safe_ping(host: str):
    # Using shlex.quote to safely escape the host parameter
    from shlex import quote
    subprocess.call(f'ping {quote(host)}')

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    safe_ping(host)
    return {'status': 'completed'}