from fastapi import FastAPI
import subprocess
from shlex import quote

class SafePing:
    def __init__(self, host: str):
        self.host = quote(host)

    def execute(self):
        try:
            output = subprocess.check_output(['ping', self.host], stderr=subprocess.STDOUT, timeout=5)
            return {'status': 'completed', 'output': output.decode()}
        except subprocess.CalledProcessError as e:
            return {'status': 'failed', 'error': e.output.decode()}
        except subprocess.TimeoutExpired as e:
            return {'status': 'timeout', 'message': 'Ping request timed out'}

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    safe_ping = SafePing(host)
    return safe_ping.execute()