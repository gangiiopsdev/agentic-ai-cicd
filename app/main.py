from fastapi import FastAPI
import subprocess
import shlex
class SafeSubprocess:
    @staticmethod
def safe_call(command: str, *args):
        args = shlex.split(command)
        return subprocess.run(args, check=True)

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    safe_command = f'ping {host}'
    SafeSubprocess.safe_call(safe_command)
    return {'status': 'completed'}