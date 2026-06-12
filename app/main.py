from fastapi import FastAPI
import subprocess

app = FastAPI()

def ping(host: str):
    # Secure implementation
    try:
        result = subprocess.run(['ping', host], check=True, capture_output=True, text=True)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': e.stderr}

@app.get("/ping")
def ping_endpoint(host: str):
    # Sanitize input to prevent command injection
    if not all(c.isalnum() or c in ('-', '.', '_') for c in host):
        return {'status': 'failed', 'error': 'Invalid hostname'}
    return ping(host)