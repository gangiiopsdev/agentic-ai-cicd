from fastapi import FastAPI
import subprocess
class PingService:
    def ping(self, host: str):
        if 'localhost' not in host and '127.0.0.1' not in host:
            return {'status': 'error', 'output': 'Host is not allowed'}
        command = ['ping', host]
        result = subprocess.run(command, capture_output=True, text=True, check=False)
        return {'status': 'completed', 'output': result.stdout}

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    ping_service = PingService()
    return ping_service.ping(host)