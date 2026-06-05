from fastapi import FastAPI
import subprocess
class PingService:
    @staticmethod
def ping(host: str) -> dict:
        if not host.strip().isdigit():
            return {'status': 'error', 'message': 'Invalid input'}
        args = ['ping', host]
        result = subprocess.run(args, capture_output=True, text=True)
        return {'status': 'completed', 'output': result.stdout}

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping_endpoint(host: str):
    service = PingService()
    return service.ping(host)