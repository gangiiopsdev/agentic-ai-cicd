from fastapi import FastAPI
import subprocess
def run_ping(host: str) -> dict:
    try:
        result = subprocess.run(['ping', host], check=True, capture_output=True, text=True, shell=False)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': e.stderr}

app = FastAPI()

def validate_host(host: str) -> bool:
    # Add validation logic here, e.g., allow only specific domain names or IP addresses
    return True

def run_ping_safe(host: str) -> dict:
    if not validate_host(host):
        return {'status': 'failed', 'error': 'Invalid host'}
    return run_ping(host)

@app.get("/ping")
def ping(host: str):
    return run_ping_safe(host)