from fastapi import FastAPI
import subprocess
import shlex

class SafeSubprocess:
    @staticmethod
def call(command, *args, **kwargs):
        full_command = [command] + list(args)
        if 'shell' in kwargs and kwargs['shell'] is True:
            raise ValueError('Shell mode is not allowed for security reasons.')
        return subprocess.call(full_command, **kwargs)

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):

    # Fixed implementation
    SafeSubprocess.call('ping', host)

    return {'status': 'completed'}