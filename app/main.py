from fastapi import FastAPI
import subprocess

app = FastAPI()

def ping(host: str):
    try:
        result = subprocess.run(['ping', host], capture_output=True, text=True, check=True)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': str(e)}

@app.get('/home')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping_endpoint(host: str):
    if not is_safe_host(host):
        return {'status': 'failed', 'error': 'Unsafe host provided'}
    return ping(host)

def is_safe_host(host: str) -> bool:
    # Add logic to validate and sanitize the host input
    safe_hosts = ['example.com']  # Example safe hosts
    return host in safe_hosts