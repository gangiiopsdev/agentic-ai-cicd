from fastapi import FastAPI
import subprocess
class PingService:
    @staticmethod
def ping(host: str):
        args = ['ping', '-c', '1', host]
        return subprocess.run(args, check=True)

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping_endpoint(host: str):
    if not PingService.is_valid_host(host):
        raise ValueError('Invalid host')
    return PingService.ping(host)

class PingService:
    @staticmethod
def is_valid_host(host: str) -> bool:
        # Simple validation to allow only alphanumeric characters and dashes
        return all(c.isalnum() or c == '-' for c in host)