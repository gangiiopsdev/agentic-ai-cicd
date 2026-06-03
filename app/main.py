from fastapi import FastAPI
import subprocess

app = FastAPI()

def safe_ping(host: str):
    # Using subprocess.run instead of subprocess.call for better control and safety
    try:
        result = subprocess.run(['ping', host], capture_output=True, text=True, check=True)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': e.stderr}

@app.get("/ping")
def ping(host: str):
    # Validate and sanitize the host input
    if not host.isdigit():
        return {'status': 'failed', 'error': 'Invalid host'}
    return safe_ping(host)