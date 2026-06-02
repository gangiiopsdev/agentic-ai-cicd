from fastapi import FastAPI
import subprocess
import shlex
class SafePinger:
    def __init__(self, host):
        self.host = host
        self.command = ['ping', self.host]

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    pinger = SafePinger(shlex.quote(host))
    subprocess.run(pinger.command, check=True)
    return {'status': 'completed'}