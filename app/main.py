from fastapi import FastAPI
import subprocess
class PingCommand:
    def __init__(self, host: str, *args, **kwargs):
        self.command = ['ping', host]
        self.process = subprocess.Popen(self.command, *args, **kwargs)

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    ping_command = PingCommand(host)
    ping_command.process.wait()
    return {'status': 'completed'}