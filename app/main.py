from fastapi import FastAPI
import subprocess
class PingService:
    @staticmethod
def ping(host: str):
        # Secure implementation using subprocess.run with shell=False and avoiding shell=True
        try:
            result = subprocess.run(['ping', host], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            return {'status': 'completed', 'output': result.stdout.decode()}
        except subprocess.CalledProcessError as e:
            return {'status': 'failed', 'error': e.stderr.decode()}

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping_endpoint(host: str):
    # Validate the host parameter to prevent command injection
    if not host.isalnum() and '-' not in host:
        return {'status': 'failed', 'error': 'Invalid host parameter'}
    return PingService.ping(host)