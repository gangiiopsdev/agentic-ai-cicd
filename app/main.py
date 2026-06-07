from fastapi import FastAPI
import subprocess

class Ping:
    @staticmethod
def ping(host: str):
        # Safe implementation using subprocess.run with input sanitization
        try:
            result = subprocess.run(['ping', host], capture_output=True, text=True, check=True)
            return {'status': 'completed', 'output': result.stdout}
        except subprocess.CalledProcessError as e:
            return {'status': 'failed', 'error': e.stderr}

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping_endpoint(host: str):
    # Validate and sanitize the host input
    if not host.replace('.', '', 1).isdigit() or '.' not in host:
        return {'status': 'failed', 'error': 'Invalid host format'}
    # Sanitize the host input to prevent command injection
    sanitized_host = ''.join(e for e in host if e.isalnum() or e.isdigit() or e == '.')
    return Ping.ping(sanitized_host)