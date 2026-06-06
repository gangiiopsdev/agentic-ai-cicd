from fastapi import FastAPI
import subprocess
import shlex
import os

class CommandSanitizer:
    @staticmethod
def sanitize(command: str) -> list:
        return [os.path.expandvars(cmd.strip()) for cmd in shlex.split(command)]

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    try:
        sanitized_host = CommandSanitizer.sanitize(f'ping {host}')
        subprocess.run(sanitized_host, check=True)
        return {'status': 'completed'}
    except subprocess.CalledProcessError as e:
        return {'error': str(e)}