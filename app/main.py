from fastapi import FastAPI
import subprocess
def ping(host: str):
    # Validate and sanitize the input to prevent command injection
    if not host.isalnum() or len(host) > 10:
        return {'status': 'failed', 'error': 'Invalid hostname'}

    try:
        result = subprocess.run(['ping', host], capture_output=True, text=True, check=True)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': str(e)}

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    # Validate and sanitize the input to prevent command injection
    if not host.isalnum() or len(host) > 10:
        return {'status': 'failed', 'error': 'Invalid hostname'}
    return ping(host)