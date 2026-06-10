from fastapi import FastAPI
import subprocess

app = FastAPI()

def safe_ping(host: str):
    # Ensure the host parameter is sanitized
    allowed_hosts = ['example.com', 'localhost']  # Replace with actual allowed hosts
    if host not in allowed_hosts:
        raise ValueError('Host not allowed')

    try:
        result = subprocess.run(['ping', host], capture_output=True, text=True, check=True)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': e.stderr}

@app.get('/ping')
def ping(host: str):
    return safe_ping(host)