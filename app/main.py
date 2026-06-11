from fastapi import FastAPI
import re
import subprocess

app = FastAPI()

def validate_host(host):
    # Enhanced validation logic to prevent command injection
    if not re.match(r'^[a-zA-Z0-9.-]+$', host):
        return False
    return True

@app.get("/ping")
def ping(host: str):
    if not validate_host(host):
        return {'status': 'error', 'message': 'Invalid host'}
    # Safe implementation with full path to ensure safe execution
    subprocess.run(['/bin/ping', '-c', '1', host], check=True, capture_output=True, text=True)
    return {'status': 'completed'}