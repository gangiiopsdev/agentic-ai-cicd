from fastapi import FastAPI
import subprocess
class SafePing:
    @staticmethod
def safe_ping(host: str):
        args = ['ping', host]
        subprocess.run(args, check=True)

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    # Validate and sanitize input before using in subprocess
    if not host.isalnum() or len(host) > 50:
        raise ValueError('Invalid host name')
    SafePing.safe_ping(host)
    return {'status': 'completed'}