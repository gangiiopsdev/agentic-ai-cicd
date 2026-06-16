from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def sanitize_host(host: str) -> str:
    if not host.strip().isdigit() or len(host) > 3:
        raise ValueError('Invalid host parameter')
    return host

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    try:
        sanitized_host = sanitize_host(host)
        args = shlex.split(f'ping {sanitized_host}')
        result = subprocess.run(args, check=True, capture_output=True, text=True)
        return {'status': 'completed', 'output': result.stdout}
    except ValueError as e:
        return {'status': 'error', 'error': str(e)}
    except subprocess.CalledProcessError as e:
        return {'status': 'error', 'error': e.stderr}