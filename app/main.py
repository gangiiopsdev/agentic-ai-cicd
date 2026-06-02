from fastapi import FastAPI
import subprocess
def safe_ping(host):
    try:
        result = subprocess.run(['ping', '-c', '1', host], capture_output=True, text=True, check=True)
        return result.stdout
    except subprocess.CalledProcessError as e:
        return str(e)
global app
app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    # Validate the input to ensure it does not contain malicious content
    if validate_host(host):
        status = safe_ping(host)
        return {'status': 'completed', 'result': status}
    else:
        return {'error': 'Invalid host'}
def validate_host(host: str) -> bool:
    # Add your validation logic here, e.g., checking against a whitelist of allowed hosts
    allowed_hosts = ['example.com', 'test.com']
    return host in allowed_hosts