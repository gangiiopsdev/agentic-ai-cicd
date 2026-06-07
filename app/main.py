from fastapi import FastAPI
import subprocess
def run_ping(host):
    try:
        result = subprocess.run(['ping', host], capture_output=True, text=True, check=True)
        return result.stdout.strip()
    except subprocess.CalledProcessError as e:
        return str(e)
app = FastAPI()
@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}
@app.get('/ping')
def ping(host: str):
    # Sanitize the host input to prevent code injection
    if not host.isalnum() or '.' in host:
        raise ValueError('Invalid hostname')
    return run_ping(host)