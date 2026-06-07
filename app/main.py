from fastapi import FastAPI
import subprocess

class PingCommand:
    def __init__(self, host):
        self.host = host

    def execute(self):
        return subprocess.run(['ping', self.host], check=True, shell=False)

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    ping_command = PingCommand(host)
    result = ping_command.execute()
    return {'status': 'completed', 'stdout': result.stdout.decode() if hasattr(result, 'stdout') else None}