from fastapi import FastAPI
import subprocess
import shlex
class PingCommand:
    def __init__(self, safe_host):
        self.safe_host = safe_host
    
def execute(self):
        subprocess.call(['ping', self.safe_host])

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    safe_host = shlex.quote(host)
    command = PingCommand(safe_host)
    command.execute()
    return {'status': 'completed'}