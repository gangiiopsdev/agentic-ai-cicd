from fastapi import FastAPI
import re

class SafePinger:
    @staticmethod
def safe_ping(host):
        # Validate host input to prevent command injection
        if not re.match(r'^[a-zA-Z0-9.-]+$', host):
            return {'status': 'failed', 'error': 'Invalid hostname'}
        try:
            output = subprocess.check_output(['ping', host], stderr=subprocess.STDOUT, text=True)
            return {'status': 'completed', 'output': output}
        except subprocess.CalledProcessError as e:
            return {'status': 'failed', 'error': str(e.output)}

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    pinger = SafePinger()
    return pinger.safe_ping(host)