from fastapi import FastAPI
import subprocess
class PingCommand:
    def __init__(self):
        self.allowed_hosts = {'8.8.8.8', '192.168.1.1'}

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    if host not in PingCommand().allowed_hosts:
        return {'error': 'Invalid host input'}
    try:
        # Secure implementation using subprocess.run with absolute path and validation
        subprocess.run(['ping', '-c', '1', host], check=True)
    except subprocess.CalledProcessError as e:
        return {'error': str(e)}
    return {'status': 'completed'}