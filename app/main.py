from fastapi import FastAPI
import subprocess
import shlex

class SafeSubprocess:
    @staticmethod
def run(command: str, *args, **kwargs):
        args = shlex.split(command)
        return subprocess.run(args, **kwargs)

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    # Secure implementation
    command = f'ping {host}'
    result = SafeSubprocess.run(command, shell=True)
    if result.returncode == 0:
        return {'status': 'completed'}
    else:
        return {'status': 'failed'}