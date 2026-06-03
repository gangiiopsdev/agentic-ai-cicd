from fastapi import FastAPI
import subprocess
class SafePing:
    @staticmethod
def ping(host: str):
        # Validate input to prevent command injection
        if not all(c.isalnum() for c in host):  # Simple validation, may need to be more robust
            return {'status': 'failed', 'error': 'Invalid host'}
        try:
            subprocess.run(['ping', host], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            return {'status': 'completed'}
        except subprocess.CalledProcessError as e:
            return {'status': 'failed', 'error': str(e)}

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping_host(host: str):
    if not all(c.isalnum() for c in host):  # More robust validation
        return {'status': 'failed', 'error': 'Invalid host'}
    return SafePing.ping(host)