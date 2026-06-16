from fastapi import FastAPI
import subprocess

app = FastAPI()

def safe_ping(host: str):
    try:
        result = subprocess.run(['ping', host], capture_output=True, text=True, check=True)
        return result.stdout
    except subprocess.CalledProcessError as e:
        return f'Error: {e}'

@app.get("/ping")
def ping(host: str):
    # Safe implementation
    if not validate_host(host):
        return {'status': 'error', 'response': 'Invalid host'}
    response = safe_ping(host)
    return {'status': 'completed', 'response': response}

def validate_host(host: str) -> bool:
    # Basic validation, improve based on requirements
    return host.replace('.', '').isalnum()