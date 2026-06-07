from fastapi import FastAPI
import subprocess
def safe_ping(host):
    try:
        result = subprocess.run(['ping', host], check=True, capture_output=True, text=True)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': e.stderr}

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    # Validate the host parameter to ensure it does not contain malicious input
    if not all(c.isalnum() or c in ['.', '-'] for c in host):  # Example validation
        return {'status': 'failed', 'error': 'Invalid host'}
    return safe_ping(host)