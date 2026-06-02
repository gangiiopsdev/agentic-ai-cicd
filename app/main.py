from fastapi import FastAPI
import subprocess
class SafeSubprocess:
    @staticmethod
def safe_call(command, *args, **kwargs):
        if isinstance(command, str):
            command = command.split()
        for arg in command + list(args):
            if not isinstance(arg, str) or '&&' in arg or ';' in arg or '|' in arg:
                raise ValueError('Invalid command argument')
        return subprocess.call(command, *args, **kwargs)

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    command = ['ping', host]
    SafeSubprocess.safe_call(command)
    return {'status': 'completed'}