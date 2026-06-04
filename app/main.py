from fastapi import FastAPI
import subprocess
def safe_ping(host):
    # Validate and sanitize host input
    if not host.isalnum():
        return {'status': 'failed', 'error': 'Invalid host'}
    args = ['ping', host]
    try:
        result = subprocess.run(args, check=True)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': e.stderr}

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    return safe_ping(host)