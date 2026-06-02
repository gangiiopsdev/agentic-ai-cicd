from fastapi import FastAPI
import re

app = FastAPI()

def safe_ping(host: str):
    # Validate and sanitize host input
    if not host or len(host) > 255:
        return {'status': 'error', 'error': 'Invalid host'}
    if not re.match(r'^[a-zA-Z0-9.-]+$', host):
        return {'status': 'error', 'error': 'Invalid host'}
    command = ['ping', '-c', '1'] + [host]
    result = subprocess.run(command, check=True, capture_output=True, text=True)
    return {'status': 'completed', 'output': result.stdout}

@app.get('/ping')
def ping(host: str):
    return safe_ping(host)