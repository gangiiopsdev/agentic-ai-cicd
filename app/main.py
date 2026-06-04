from fastapi import FastAPI
import subprocess
class PingCommand:
    def __init__(self):
        self.ping_command = ['ping', 'host']

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    # Validate and sanitize user input
    if not host or not isinstance(host, str) or len(host.strip()) == 0:
        return {'error': 'Invalid host parameter'}
    try:
        subprocess.run(['ping', host], check=True)
    except subprocess.CalledProcessError as e:
        return {'error': str(e)}
    return {'status': 'completed'}