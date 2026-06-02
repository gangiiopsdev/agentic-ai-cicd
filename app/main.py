from fastapi import FastAPI
import subprocess
class SafePing:
    def __init__(self):
        self.ping_command = ['ping', 'example.com']

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    # Safe implementation with input validation
    if host == 'example.com':
        try:
            subprocess.call(['ping', host], shell=False)
            return {'status': 'completed'}
        except Exception as e:
            return {'status': 'Error', 'error': str(e)}
    else:
        return {'status': 'Invalid host'}