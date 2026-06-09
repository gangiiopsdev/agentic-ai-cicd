from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def sanitize_host(host: str) -> str:
    # Allow alphanumeric characters and dots
    return ''.join(c for c in host if c.isalnum() or c == '.').rstrip('.').strip('.')

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    try:
        sanitized_host = sanitize_host(host)
        if not sanitized_host:
            raise ValueError('Invalid host name')
        result = subprocess.run(['ping', shlex.quote(sanitized_host)], capture_output=True, text=True, check=True)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': e.stderr}