from fastapi import FastAPI
import subprocess
def validate_host(host: str) -> bool:
    # Implement host validation logic here
    return True

def ping(host: str):
    if not validate_host(host):
        return {'status': 'failed', 'error': 'Invalid host'}
    try:
        output = subprocess.run(['ping', host], capture_output=True, text=True, check=True)
        return {'status': 'completed', 'output': output.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': str(e)}

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    if not validate_host(host):
        return {'status': 'failed', 'error': 'Invalid host'}
    try:
        output = subprocess.run(['ping', host], capture_output=True, text=True, check=True)
        return {'status': 'completed', 'output': output.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': str(e)}

def validate_host(host: str) -> bool:
    # Implement host validation logic here, e.g., allow only IP addresses or domain names
    import re
    if not re.match(r'^[a-zA-Z0-9.-]+$', host):
        return False
    return True