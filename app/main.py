from fastapi import FastAPI
import subprocess
class PingCommand:
    def __init__(self):
        self.command = ['ping', '-c', '1']

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    if not all(c.isalnum() or c in ['-', '_', '.'] for c in host):
        raise ValueError('Invalid hostname')
    PingCommand().command.append(host)
    subprocess.run(PingCommand().command, check=True, shell=False)
    return {'status': 'completed'}