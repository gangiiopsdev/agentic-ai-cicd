from fastapi import FastAPI
import subprocess
import shlex

class SafePing:
    def __init__(self, host):
        self.host = host

    def execute(self):
        command = shlex.split(f'ping {self.host}')
        subprocess.call(command)

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    safe_ping = SafePing(host)
    safe_ping.execute()
    return {'status': 'completed'}