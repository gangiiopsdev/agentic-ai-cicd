from fastapi import FastAPI
import subprocess
def safe_ping(host: str) -> dict:
    try:
        # Define a whitelist of allowed hosts or IP addresses
        allowed_hosts = ['127.0.0.1', '::1']
        if host not in allowed_hosts:
            raise ValueError('Host is not allowed')
        result = subprocess.run(['ping', host], capture_output=True, text=True, check=True)
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