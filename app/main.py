from fastapi import FastAPI
import subprocess

app = FastAPI()

def safe_ping(host: str):
    try:
        output = subprocess.check_output(['ping', host], stderr=subprocess.STDOUT, text=True)
        return {'status': 'completed', 'output': output}
    except subprocess.CalledProcessError as e:
        return {'status': 'error', 'error': e.output}

@app.get("/ping")
def ping(host: str):
    # Validate host input to prevent injection attacks
    if not validate_host(host):
        return {'status': 'error', 'error': 'Invalid host'}
    return safe_ping(host)

# Simple validation function for demonstration purposes
def validate_host(host: str) -> bool:
    return host.strip() and all(c.isalnum() or c in ('.', '-') for c in host)