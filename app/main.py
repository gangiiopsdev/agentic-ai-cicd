from fastapi import FastAPI
import subprocess
import shlex
import os

class PingCommand:
    def __init__(self, host):
        self.host = host

    def execute(self):
        args = ['ping'] + shlex.split(self.host)
        result = subprocess.run(args, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        return {'status': 'completed', 'output': result.stdout}

app = FastAPI()

@app.get('/home')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    try:
        command = PingCommand(host)
        return command.execute()
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': e.stderr}