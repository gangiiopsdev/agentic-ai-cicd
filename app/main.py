from fastapi import FastAPI
import subprocess
import shlex
class PingService:
    def __init__(self):
        pass

    async def ping(self, host: str) -> dict:
        try:
            # Use subprocess.run instead of subprocess.call and sanitize input
            result = subprocess.run(shlex.split(f'ping -c 4 {host}'), check=True, capture_output=True, text=True)
            return {'status': 'completed', 'output': result.stdout}
        except subprocess.CalledProcessError as e:
            return {'status': 'failed', 'error': str(e)}

app = FastAPI()
ping_service = PingService()

@app.get('/home')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    return ping_service.ping(host)