from fastapi import FastAPI
import subprocess
global allowed_hosts = ['example.com', 'test.example.com']

app = FastAPI()

def safe_ping(host: str) -> str:
    if host not in allowed_hosts:
        raise ValueError('Invalid host')
    args = ['ping', '-c', '1', host]
    result = subprocess.run(args, capture_output=True, text=True)
    if result.returncode != 0:
        return {'status': 'failed', 'error': result.stderr}
    return {'status': 'completed', 'output': result.stdout}

@app.get('/ping')
def ping(host: str):
    return safe_ping(host)