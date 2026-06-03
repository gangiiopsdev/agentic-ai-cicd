from fastapi import FastAPI
import subprocess
class CommandExecutor:
    def __init__(self):
        self.allowed_hosts = ['127.0.0.1', '::1']

    async def ping(self, host: str):
        if host in self.allowed_hosts:
            args = ['ping', host]
            subprocess.call(args)
        else:
            return {'status': 'error', 'message': 'Host not allowed'}

app = FastAPI()
executor = CommandExecutor()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    return executor.ping(host)