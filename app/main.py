from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

global_ping_command = 'ping'

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    try:
        args = [global_ping_command, '-c', '1'] + shlex.split(host)
        subprocess.run(args, check=True)
        return {'status': 'completed'}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': str(e)}