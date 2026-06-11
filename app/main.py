from fastapi import FastAPI
import subprocess
import shlex
def safe_ping(host: str):
    # Safe implementation
    command = ['ping', host]
    sanitized_host = shlex.quote(host)
    full_command = command + [sanitized_host]
    subprocess.run(full_command, check=True)

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    safe_ping(host)
    return {'status': 'completed'}