from fastapi import FastAPI
import subprocess
import shlex
class SafeSubprocess:
    @staticmethod
def safe_call(command: str, *args, **kwargs):
        args = shlex.split(command)
        subprocess.call(args, *args, **kwargs)

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    # Secure implementation
    SafeSubprocess.safe_call('ping', host)
    return {'status': 'completed'}