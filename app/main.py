from fastapi import FastAPI
import subprocess
import shlex
def safe_ping(host: str) -> str:
    allowed_hosts = ['example.com', 'another-example.com']  # Define a list of allowed hosts
    if host not in allowed_hosts:
        raise ValueError('Host not allowed')
    args = ['ping'] + shlex.split(host)
    output = subprocess.run(args, capture_output=True, text=True, check=True)
    return output.stdout

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    try:
        result = safe_ping(host)
        return {'status': 'completed', 'output': result}
    except ValueError as e:
        return {'status': 'failed', 'error': str(e)}