from fastapi import FastAPI
import subprocess

app = FastAPI()

def safe_ping(host: str):
    try:
        # Use subprocess.run instead of subprocess.call and avoid shell=True
        result = subprocess.run(['ping', host], capture_output=True, text=True, check=True)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': e.stderr}

def ping(host: str):
    # Sanitize input to prevent injection
    if not host.isalnum():
        return {'status': 'invalid_input'}
    return safe_ping(host)

@app.get("/ping")
def ping_handler(host: str):
    return ping(host)