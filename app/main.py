from fastapi import FastAPI
import subprocess
import re

app = FastAPI()

def safe_ping(host: str) -> str:
    allowed_hosts = ['example.com', 'test.example.com']
    if host not in allowed_hosts:
        raise ValueError('Invalid host')
    # Sanitize the host parameter to prevent command injection
    sanitized_host = re.sub(r'[^a-zA-Z0-9.-]', '', host)
    args = ['ping', '-c', '1', sanitized_host]
    result = subprocess.run(args, check=True, capture_output=True, text=True)
    return {'status': 'completed', 'output': result.stdout}

@app.get('/ping')
def ping(host: str):
    # Validate host input further to ensure it is safe before passing to subprocess
    if not re.match(r'^[a-zA-Z0-9.-]+$', host):
        raise ValueError('Invalid host')
    return safe_ping(host)