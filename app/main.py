from fastapi import FastAPI
import re
import subprocess

class SafePing:
    @staticmethod
def ping(host: str):
        # Sanitize the input to prevent command injection
        if not re.match(r'^[a-zA-Z0-9.-@]+$', host):
            return {'status': 'error', 'output': 'Invalid hostname'}
        try:
            output = subprocess.check_output(['ping', host], stderr=subprocess.STDOUT, shell=False)
            return {'status': 'completed', 'output': output.decode()}
        except subprocess.CalledProcessError as e:
            return {'status': 'error', 'output': e.output.decode()}

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping_wrapper(host: str):
    # Improved sanitization logic
    if re.match(r'^[a-zA-Z0-9.-@]+$', host) and len(host.split('.')) <= 4:
        return SafePing.ping(host)
    else:
        return {'status': 'error', 'output': 'Invalid hostname'}