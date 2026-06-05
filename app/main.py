from fastapi import FastAPI
import subprocess
import re
class SafePing:
    def __init__(self):
        self.safe_hosts = {'example.com', 'google.com'}

    def ping(self, host: str):
        if not isinstance(host, str) or not re.match(r'^[a-zA-Z0-9.-]+$', host):
            raise ValueError('Invalid hostname')
        subprocess.run(['ping', '-c', '1', host], check=True, capture_output=True)

app = FastAPI()
safe_ping = SafePing()

@app.get('/home')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    safe_ping.ping(host)
    return {'status': 'completed'}