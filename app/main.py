from fastapi import FastAPI
import subprocess
import re

app = FastAPI()

def safe_ping(host):
    try:
        result = subprocess.run(['ping', host], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return {'status': 'completed', 'stdout': result.stdout.decode(), 'stderr': result.stderr.decode()}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': str(e)}

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Validate or sanitize the host input before using it in subprocess call
    if not validate_host(host):
        return {'status': 'failed', 'error': 'Invalid host'}
    return safe_ping(host)

# Function to validate host input
def validate_host(host: str) -> bool:
    # Example simple regex for validation, adjust as needed
    pattern = r'^[a-zA-Z0-9.-]+$'
    return re.match(pattern, host) is not None