from fastapi import FastAPI
import subprocess
def validate_host(host):
    allowed_hosts = ['google.com', 'example.com']
    if host not in allowed_hosts:
        raise ValueError('Invalid host')

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    validate_host(host)
    args = ['ping', '-c', '1', host]  # Limit the number of pings to avoid abuse
    result = subprocess.run(args, capture_output=True, text=True, check=True)  # Use check=True for better error handling
    return {'status': 'completed', 'output': result.stdout}