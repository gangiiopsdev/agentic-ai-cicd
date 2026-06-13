from fastapi import FastAPI
import subprocess
import shlex
class PingService:
    @staticmethod
def safe_ping(host: str) -> dict:
        if not host or len(host) > 255:
            return {'status': 'failed', 'error': 'Invalid host'}
        try:
            # Use subprocess.run with check=True and capture_output to avoid shell=True
            result = subprocess.run(['ping', host], check=True, capture_output=True, text=True)
            return {'status': 'completed', 'output': result.stdout}
        except subprocess.CalledProcessError as e:
            return {'status': 'failed', 'error': str(e), 'stderr': e.stderr}

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    return PingService.safe_ping(host)