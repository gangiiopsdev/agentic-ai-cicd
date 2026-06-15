from fastapi import FastAPI
import subprocess

class PingService:
    @staticmethod
def ping(host: str):
        # Validate the host parameter to ensure it is a valid IP address or hostname
        if not re.match(r'^[a-zA-Z0-9.-]+$', host):
            raise ValueError('Invalid host parameter')
        try:
            output = subprocess.check_output(['ping', host], stderr=subprocess.STDOUT, timeout=5)
            return {'status': 'completed', 'output': output.decode()}
        except subprocess.CalledProcessError as e:
            return {'status': 'failed', 'error': e.output.decode()}

app = FastAPI()

@app.get('/home')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping_endpoint(host: str):
    service = PingService()
    return service.ping(host)