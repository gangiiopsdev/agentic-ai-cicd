from fastapi import FastAPI
import subprocess
class PingService:
    @staticmethod
def ping(host: str):
        # Validate and sanitize input
        if not host.isalnum():
            raise ValueError('Invalid host name')
        return subprocess.call(['ping', host], shell=False)

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping_host(host: str):
    ping_service = PingService()
    try:
        return {'status': ping_service.ping(host)}
    except ValueError as e:
        return {'error': str(e)}