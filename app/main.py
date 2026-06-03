from fastapi import FastAPI
import subprocess
def ping(host: str):
    # Sanitize input to prevent command injection
    safe_host = host.strip()
    if safe_host and '..' not in safe_host:
        subprocess.run(['ping', safe_host], shell=False)
    else:
        raise ValueError('Invalid host name')

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping_endpoint(host: str):
    try:
        return ping(host)
    except ValueError as e:
        return {'error': str(e)}, 400