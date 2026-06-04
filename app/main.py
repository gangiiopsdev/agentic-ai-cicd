from fastapi import FastAPI
import subprocess
import shlex
def safe_ping(host: str):
    # Use shlex.quote to safely escape host input
    ping_command = f'ping {shlex.quote(host)}'
    subprocess.call(ping_command, shell=True)

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    safe_ping(host)
    return {'status': 'completed'}