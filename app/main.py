from fastapi import FastAPI
import subprocess
def safe_ping(host: str):
    if host not in ['example.com', 'test.com']:  # Limit to specific trusted hosts
        return 'Invalid host'
    try:
        result = subprocess.run(['ping', '-c', '1', host], check=True, capture_output=True, text=True)
        return result.stdout
    except subprocess.CalledProcessError as e:
        return f'Ping failed with error: {e.stderr}'

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    # Validate host input to ensure it does not contain malicious content
    import re
    if not re.match(r'^[a-zA-Z0-9.-]+$', host):
        return 'Invalid host'
    return safe_ping(host)