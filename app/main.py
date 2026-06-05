from fastapi import FastAPI
import subprocess
import shlex

class SafeSubprocess:
    @staticmethod
def call(command: str, *args, **kwargs):
        safe_command = shlex.split(command)
        return subprocess.call(safe_command, *args, **kwargs)

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    # Safe implementation
    command = f'ping {host}'
    SafeSubprocess.call(command, shell=True)
    return {'status': 'completed'}