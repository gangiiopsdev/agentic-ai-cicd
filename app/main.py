from fastapi import FastAPI
import subprocess

app = FastAPI()

def safe_ping(host):
    if not validate_host(host):
        return 'Invalid host'
    try:
        result = subprocess.run(['ping', host], capture_output=True, text=True, check=True)
        return result.stdout
    except subprocess.CalledProcessError as e:
        return f'Ping failed: {e}'

@app.get("/ping")
def ping(host: str):
    return {'status': safe_ping(host)}

def validate_host(host):
    # Add validation logic here, e.g., regex to allow only valid IP addresses or hostnames
    import re
    pattern = r'^[a-zA-Z0-9.-]+$'
    return re.match(pattern, host) is not None