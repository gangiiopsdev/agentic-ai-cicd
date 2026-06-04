from fastapi import FastAPI
import subprocess
import shlex

class SafePing:
    def __init__(self, host: str):
        self.host = host

    def execute(self):
        command = ['ping', self.host]
        args = shlex.split(' '.join(command))
        subprocess.run(args, check=True)

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    safe_ping = SafePing(host)
    safe_ping.execute()
    return {'status': 'completed'}