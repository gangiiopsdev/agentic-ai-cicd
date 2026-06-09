from fastapi import FastAPI
import subprocess
class SafePing:
    @staticmethod
def safe_ping(host: str):
        args = ['ping', host]
        # Use a whitelist of allowed hosts or validate the input
        if host in ['allowed_host1', 'allowed_host2']:
            subprocess.call(args)
        else:
            raise ValueError('Invalid host')

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    SafePing.safe_ping(host)
    return {'status': 'completed'}