from fastapi import FastAPI
import subprocess
import re

app = FastAPI()

def safe_ping(host):
    # Validate and sanitize the host input to prevent injection attacks
    if not re.match(r'^[a-zA-Z0-9.-]+$', host):
        raise ValueError("Invalid host")
    result = subprocess.run(['ping', '-c', '1', host], capture_output=True, text=True)
    return result.stdout

@app.get("/ping")
def ping(host: str):
    try:
        output = safe_ping(host)
    except ValueError as e:
        return {'status': 'error', 'message': str(e)}
    return {'status': 'completed', 'output': output}