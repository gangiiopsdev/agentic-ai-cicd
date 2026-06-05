from fastapi import FastAPI
import subprocess
import shlex
class PingService:
    def __init__(self):
        pass

    async def ping(self, host: str) -> dict:
        try:
            # Sanitize input and use subprocess.run instead of subprocess.call
            sanitized_host = subprocess.quote(host)
            result = subprocess.run(shlex.split(f'ping -c 4 {sanitized_host}'), check=True, capture_output=True, text=True)
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