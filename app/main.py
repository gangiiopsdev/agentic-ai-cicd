from fastapi import FastAPI
import subprocess
import shlex
import os

class PingCommand:
    def __init__(self, host):
        self.host = host

    def execute(self):
        if '@' in self.host or ':' in self.host:
            raise ValueError('Invalid input')
        args = shlex.split(f'ping {self.host}')
        subprocess.call(args)

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    try:
        ping_command = PingCommand(host)
        ping_command.execute()
        return {'status': 'completed'}
    except ValueError as e:
        return {'error': str(e)}