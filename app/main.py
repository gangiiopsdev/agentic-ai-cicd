from fastapi import FastAPI
import subprocess
from shlex import quote
generate_ping_command = lambda host: f'ping {quote(host)}'

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    try:
        subprocess.call(generate_ping_command(host), shell=False)
    except Exception as e:
        return {'status': 'failed', 'error': str(e)}
    return {'status': 'completed'}