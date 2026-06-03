from fastapi import FastAPI
import subprocess
import re
class SafePing:
    def __init__(self):
        self.safe_hosts = {'example.com', 'google.com'}

    def ping(self, host: str):
        if host not in self.safe_hosts:
            raise ValueError('Invalid hostname')
        subprocess.run(['ping', host], check=True, capture_output=True)

app = FastAPI()
safe_ping = SafePing()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    safe_ping.ping(host)
    return {'status': 'completed'}