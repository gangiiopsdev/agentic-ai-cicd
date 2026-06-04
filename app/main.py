from fastapi import FastAPI
import subprocess
git_command = f'ping {host}'

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    # Safe implementation using shlex.quote to escape the input
    import shlex
    safe_command = ['ping', shlex.quote(host)]
    subprocess.call(safe_command)
    return {'status': 'completed'}