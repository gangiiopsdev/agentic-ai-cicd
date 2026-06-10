from fastapi import FastAPI
import subprocess

app = FastAPI()

def safe_ping(host: str):
    # Validate the host to ensure it's a trusted format (e.g., IP address or domain name)
    if not is_valid_host(host):
        raise ValueError('Invalid host')

    try:
        result = subprocess.run(['ping', host], capture_output=True, text=True, check=True, shell=False)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': e.stderr}

@app.get("/ping")
def ping(host: str):
    return safe_ping(host)

def is_valid_host(host: str) -> bool:
    # Implement host validation logic here
    import re
    pattern = r'^[a-zA-Z0-9.-]+$'
    return re.match(pattern, host) is not None