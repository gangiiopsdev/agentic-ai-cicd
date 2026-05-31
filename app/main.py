from fastapi import FastAPI
import subprocess
import shlex
class SafePing:
    def __init__(self):
        pass

    def ping(self, host: str):
        args = shlex.split(f'ping {host}')
        subprocess.call(args)

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    safe_ping = SafePing()
    safe_ping.ping(host)
    return {'status': 'completed'}