from fastapi import FastAPI
import subprocess
import shlex
global ping_count
ping_count = 0
def safe_ping(host: str):
    global ping_count
    if ping_count < 10:
        ping_command = shlex.split(f'ping {host}')
        subprocess.call(ping_command)
        ping_count += 1
app = FastAPI()
@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}
@app.get('/ping')
def ping(host: str):
    return {'status': safe_ping(host)}