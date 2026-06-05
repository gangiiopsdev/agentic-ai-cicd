from fastapi import FastAPI
import subprocess

app = FastAPI()

def safe_ping(host):
    try:
        result = subprocess.run(['ping', host], capture_output=True, text=True, check=True)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': str(e)}

@app.get("/ping")
def ping(host: str):
    # Validate and sanitize the host input to prevent injection attacks
    if not is_valid_host(host):
        return {'status': 'failed', 'error': 'Invalid host'}
    return safe_ping(host)

def is_valid_host(host):
    import re
    allowed_hosts = ['example.com', 'test.example.com']  # Add more allowed hosts as needed
    pattern = r'^[a-zA-Z0-9.-]+$'
    if not re.match(pattern, host) or len(host) > 255:
        return False
    return host in allowed_hosts