from fastapi import FastAPI
import subprocess
def safe_ping(host: str):
    # Validate host input
    if not is_valid_host(host):
        raise ValueError('Invalid host')
    args = ['ping', host]
    result = subprocess.run(args, capture_output=True, text=True)
    if result.returncode != 0:
        raise Exception(f'Ping failed: {result.stderr}')

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    safe_ping(host)
    return {'status': 'completed'}
def is_valid_host(host: str) -> bool:
    # Simple validation example, adjust as needed
    allowed_hosts = ['example.com', 'localhost']
    return host in allowed_hosts