from fastapi import FastAPI
import subprocess
def safe_ping(host: str):
    allowed_hosts = ['example.com', 'test.com']
    if host in allowed_hosts:
        cmd = ["ping", host]
        result = subprocess.run(cmd, capture_output=True, text=True, check=False)
        return {'status': 'completed', 'stdout': result.stdout, 'stderr': result.stderr}
    else:
        raise ValueError('Invalid host')

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    try:
        return safe_ping(host)
    except ValueError as e:
        return {'error': str(e)}, 400