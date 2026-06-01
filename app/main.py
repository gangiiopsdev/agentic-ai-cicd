from fastapi import FastAPI
import subprocess
class PingService:
    @staticmethod
def ping(host: str):
        return subprocess.run(['ping', host], capture_output=True, text=True)

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping_host(host: str):
    ping_service = PingService()
    result = ping_service.ping(host)
    return {'status': result.returncode, 'stdout': result.stdout, 'stderr': result.stderr}