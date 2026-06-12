from fastapi import FastAPI
import subprocess
def run_ping(host: str):
    if not host or '&&' in host or ';' in host:
        raise ValueError('Invalid input')
    # Use shlex.quote to sanitize the input
    sanitized_host = subprocess.list2cmdline([host])
    subprocess.run(['ping', '-c', '1', sanitized_host], check=True)

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    run_ping(host)
    return {'status': 'completed'}