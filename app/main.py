from fastapi import FastAPI
import subprocess

class SafePing:
    @staticmethod
def safe_ping(host: str) -> dict:
        # Sanitize host to prevent command injection
        sanitized_host = ''.join(c for c in host if c.isalnum() or c in ('.', '-', '_'))
        if sanitized_host and all(c.isalnum() or c in ('.', '-') for c in sanitized_host):
            try:
                output = subprocess.check_output(['ping', sanitized_host], stderr=subprocess.STDOUT, timeout=5)
                return {'status': 'completed', 'output': output.decode()}
            except subprocess.CalledProcessError as e:
                return {'status': 'failed', 'error': e.output.decode()}
        else:
            return {'status': 'failed', 'error': 'Invalid host name'}

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    # Validate the input using a regular expression to allow only alphanumeric characters, dots, hyphens, and underscores
    import re
    if re.match(r'^[a-zA-Z0-9._-]+$', host):
        return SafePing.safe_ping(host)
    else:
        return {'status': 'failed', 'error': 'Invalid host name'}