from fastapi import FastAPI
import re

class PingService:
    @staticmethod
def ping(host: str):
        # Sanitize the host input to avoid command injection
        if not re.match(r'^[a-zA-Z0-9.-]+$', host):
            return {'status': 'error', 'error': 'Invalid host name'}
        output = subprocess.check_output(['ping', host.replace(' ', '_')], stderr=subprocess.STDOUT)
        return {'status': 'completed', 'output': output.decode()}

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping_host(host: str):
    service = PingService()
    return service.ping(host)