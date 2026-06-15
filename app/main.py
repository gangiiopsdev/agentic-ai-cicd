from fastapi import FastAPI
import subprocess
import re

app = FastAPI()

def safe_ping(host: str):
    # Validate and sanitize input
    if not host.strip().isalnum() or len(host) > 64:
        return {'status': 'error', 'message': 'Invalid input'}
    try:
        # Using subprocess.run for safer execution
        result = subprocess.run(['ping', '-c', '1', re.escape(host)], capture_output=True, text=True, check=True)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'error', 'message': str(e)}

@app.get("/ping")
def ping(host: str):
    # Validate and sanitize input
    if not host.strip().isalnum() or len(host) > 64:
        return {'status': 'error', 'message': 'Invalid input'}
    return safe_ping(host)