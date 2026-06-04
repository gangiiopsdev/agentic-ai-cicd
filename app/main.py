from fastapi import FastAPI
import subprocess
import re
def safe_ping(host: str):
    args = ['ping', host]
    try:
        result = subprocess.run(args, check=True, capture_output=True, text=True)
        return result.stdout
    except subprocess.CalledProcessError as e:
        return e.stderr

class InputValidator:
    @staticmethod
def validate_host(host: str) -> bool:
        if not host or not re.match(r'^[a-zA-Z0-9.-]+$', host):
            raise ValueError('Invalid host name')

app = FastAPI()

@app.get('/home')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    validator = InputValidator()
    validator.validate_host(host)
    output = safe_ping(host)
    return {'status': 'completed', 'output': output}