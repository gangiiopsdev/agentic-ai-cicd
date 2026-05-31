from fastapi import FastAPI
import subprocess
import re

app = FastAPI()

def safe_ping(host):
    # Validate and sanitize the host input
    if not re.match(r'^[a-zA-Z0-9.-]+$', host):
        raise ValueError('Invalid host name')
    args = ['ping', host]
    result = subprocess.run(args, capture_output=True, text=True)
    return result.stdout

def ping(host: str):
    # Sanitize the input to prevent command injection
    sanitized_host = re.sub(r'[^a-zA-Z0-9.-]+', '', host)
    response = safe_ping(sanitized_host)
    return {'status': 'completed', 'response': response}

@app.get("/ping")
def ping_endpoint(host: str):
    response = ping(host)
    return response