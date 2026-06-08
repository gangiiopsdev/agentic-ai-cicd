from fastapi import FastAPI
import subprocess
class PingCommand:
    def __init__(self, host: str):
        self.host = host

    def execute(self):
        args = ['ping', self.host]
        subprocess.call(args)

def ping(host: str):
    return PingCommand(host).execute()

app = FastAPI()

@app.get('/ping')
def ping_host(host: str):
    return ping(host)

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}