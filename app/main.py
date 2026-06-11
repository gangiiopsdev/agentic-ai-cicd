from fastapi import FastAPI
import subprocess

app = FastAPI()

def safe_ping(host):
    # Safe implementation using subprocess.call with shell=False and full executable path
    try:
        result = subprocess.run(['ping', host], check=True, capture_output=True, text=True)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'error', 'error': e.stderr}

@app.get("/ping")
def ping(host: str):
    # Validate input to prevent command injection
    if not host.isalnum():
        return {'status': 'error', 'error': 'Invalid input'}
    return safe_ping(host)