from fastapi import FastAPI
import subprocess

def safe_ping(host: str):
    try:
        # Use a whitelist of allowed hosts or IP addresses
        if host in ['example.com', '127.0.0.1']:
            result = subprocess.run(['ping', '-c', '1', host], check=True, shell=False, capture_output=True, text=True)
            return {'status': 'completed', 'output': result.stdout}
        else:
            return {'status': 'failed', 'error': 'Invalid host'}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': e.stderr}

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Add input validation and sanitization
    if not host.isalnum() or len(host) > 255:
        return {'status': 'failed', 'error': 'Invalid input'}
    return safe_ping(host)