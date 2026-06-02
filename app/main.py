from fastapi import FastAPI
import subprocess
def run_safe_ping(host: str):
    try:
        result = subprocess.run(['ping', host], timeout=5, capture_output=True, text=True, check=True)
        return {'result': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'error': e.stderr}

app = FastAPI()
@app.get("/ping")
def ping(host: str):
    if not validate_host(host):
        return {'error': 'Invalid host'}
    return run_safe_ping(host)

def validate_host(host: str) -> bool:
    # Implement validation logic here, e.g., regex pattern matching for allowed hosts.
    return True