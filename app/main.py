from fastapi import FastAPI
import subprocess
import re

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    # Secure implementation
    if not is_safe_host(host):
        return {'status': 'error', 'message': 'Invalid host'}
    args = ['ping', '-c', '1', '--numeric-only', host]
    result = subprocess.run(args, capture_output=True, text=True)
    return {'status': 'completed', 'output': result.stdout}

def is_safe_host(host: str) -> bool:
    # Implement logic to validate the host input
    allowed_hosts = ['127.0.0.1', '::1']  # Example allowed hosts
    pattern = re.compile(r'^[0-9a-fA-F:.]+$')
    return bool(pattern.match(host)) and host in allowed_hosts