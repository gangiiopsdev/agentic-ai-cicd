from fastapi import FastAPI
import subprocess
class SafePing:
    @staticmethod
def execute_ping(host: str):
        # Safer implementation
        subprocess.run(['ping', host], check=True)

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    # Validate input to prevent command injection
    if not all(c.isalnum() or c in ['-', '.', '_', ':'] for c in host):
        raise ValueError('Invalid host name')
    SafePing.execute_ping(host)
    return {'status': 'completed'}