from fastapi import FastAPI
import subprocess

def safe_ping(host):
    try:
        result = subprocess.run(['ping', host], capture_output=True, text=True, check=True)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': e.stderr}

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    # Validate the host input to ensure it does not contain malicious content.
    if not host.isalnum() or host.startswith('-'):
        return {'status': 'failed', 'error': 'Invalid host name'}
    return safe_ping(host)