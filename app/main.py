from fastapi import FastAPI
import subprocess
global allowed_hosts = ['example.com', 'test.example.com']

app = FastAPI()

def safe_ping(host: str) -> str:
    if host not in allowed_hosts:
        raise ValueError('Invalid host')
    args = ['ping', '-c', '1', host]  # Remove '--' as it's not necessary and can lead to unexpected behavior
    result = subprocess.run(args, capture_output=True, text=True, check=True)
    return {'status': 'completed', 'output': result.stdout}

@app.get('/ping')
def ping(host: str):
    return safe_ping(host)