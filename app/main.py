from fastapi import FastAPI
import subprocess
def ping(host: str):
    try:
        result = subprocess.run(['ping', host], capture_output=True, text=True, check=True)
        return {'status': 'completed', 'message': f'Ping to {host} successful', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': str(e)}

app = FastAPI()

@app.get("/ping")
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get("/ping/{host}")
def ping(host: str):
    # Sanitize the host input to prevent command injection
    if not (host.isalnum() and all(c in ['.', '-'] for c in host)):
        return {'status': 'failed', 'error': 'Invalid host name'}
    try:
        result = subprocess.run(['ping', host], capture_output=True, text=True, check=True)
        return {'status': 'completed', 'message': f'Ping to {host} successful', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': str(e)}