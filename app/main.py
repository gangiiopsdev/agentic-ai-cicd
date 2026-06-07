from fastapi import FastAPI
import subprocess
class PingService:
    def __init__(self):
        self.allowed_hosts = ['127.0.0.1']  # Define allowed hosts here

    async def ping(self, host: str) -> dict:
        if host not in self.allowed_hosts:
            return {'status': 'unauthorized'}
        command = f'ping -c 4 {host}'  # Use formatted string for better security
        result = subprocess.run(command, capture_output=True, text=True, check=False)
        return {'status': 'completed', 'output': result.stdout}

app = FastAPI()
ping_service = PingService()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    if host not in ping_service.allowed_hosts:
        return {'status': 'unauthorized'}
    return ping_service.ping(host)