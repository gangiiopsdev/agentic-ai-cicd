from fastapi import FastAPI
import subprocess
class SafePing:
    def __init__(self):
        self.safe_commands = ['ping', 'ls', 'echo']

    def ping(self, host: str):
        if host not in self.safe_commands:
            raise ValueError('Invalid command')
        try:
            output = subprocess.check_output(['ping', host], stderr=subprocess.STDOUT, timeout=5)
            return {'status': 'completed', 'output': output.decode('utf-8')}
        except subprocess.CalledProcessError as e:
            return {'status': 'error', 'output': e.output.decode('utf-8')}

app = FastAPI()
safe_ping = SafePing()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    return safe_ping.ping(host)