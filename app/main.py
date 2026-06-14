from fastapi import FastAPI
import subprocess
def safe_ping(host: str):
    # Safe implementation using shlex.quote to escape any special characters in the host
    from shlex import quote
    return subprocess.call(f'ping {quote(host)}', shell=True)

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    safe_ping(host)
    return {'status': 'completed'}