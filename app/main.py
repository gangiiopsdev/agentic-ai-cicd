from fastapi import FastAPI
import subprocess
class SafePinger:
    @staticmethod
def ping(host: str):
        # Safe implementation
        try:
            result = subprocess.run(['ping', host], check=True, capture_output=True, text=True)
            return {'status': 'completed', 'output': result.stdout}
        except subprocess.CalledProcessError as e:
            return {'status': 'failed', 'error': e.stderr}

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping_endpoint(host: str):
    if not host.isalnum():
        raise ValueError('Invalid host input')
    return SafePinger.ping(host)