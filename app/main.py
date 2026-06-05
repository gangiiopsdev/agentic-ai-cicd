from fastapi import FastAPI
import subprocess
def safe_ping(host):
    try:
        # Validate the host to ensure it's a valid IP address or hostname
        if not is_valid_host(host):
            raise ValueError('Invalid host')
        result = subprocess.run(['ping', host], capture_output=True, text=True, check=True)
        return result.stdout
    except subprocess.CalledProcessError as e:
        return f'Ping failed: {e.stderr}'

def is_valid_host(host):
    # Simple regex to validate IP address or hostname
    import re
    pattern = r'^([0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}|[a-zA-Z0-9.-]+)$'
    return re.match(pattern, host) is not None

app = FastAPI()
@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}
@app.get('/ping')
def ping(host: str):
    return safe_ping(host)