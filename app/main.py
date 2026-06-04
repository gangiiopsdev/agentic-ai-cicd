from fastapi import FastAPI
import subprocess

app = FastAPI()
@app.get("/ping")
def ping(host: str):
    allowed_hosts = ['example.com', 'test.example.com']
    if host not in allowed_hosts:
        raise ValueError("Invalid host")
    command = ['ping', '-c', '1', host]
    # Validate and sanitize the input before using subprocess
    if not is_valid_host(host):
        raise ValueError("Invalid host")
    result = subprocess.run(command, check=True, capture_output=True, text=True)
    return {'status': 'completed', 'output': result.stdout}

def is_valid_host(hostname: str) -> bool:
    # Add logic to validate the hostname
    import re
    pattern = r'^[a-zA-Z0-9.-]+$'
    if not re.match(pattern, hostname):
        return False
    return True