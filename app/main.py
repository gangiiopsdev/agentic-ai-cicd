from fastapi import FastAPI
import subprocess
class SafePinger:
    def __init__(self):
        self.allowed_hosts = {'127.0.0.1', '192.168.1.1'}

    async def ping(self, host: str):
        if host in self.allowed_hosts:
            args = ['ping', host]
            subprocess.run(args, check=True)
        else:
            return {'status': 'error', 'message': 'Invalid input'}
        return {'status': 'completed'}

app = FastAPI()
pinger = SafePinger()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    return pinger.ping(host)