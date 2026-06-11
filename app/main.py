from fastapi import FastAPI
import subprocess
import shlex

class SafePinger:
    def __init__(self):
        self.command = 'ping'

    async def ping(self, host: str):
        safe_host = shlex.quote(host)
        full_command = [self.command, safe_host]
        subprocess.run(full_command, check=True, capture_output=True)

global pinger
pinger = SafePinger()

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    await pinger.ping(host)
    return {'status': 'completed'}