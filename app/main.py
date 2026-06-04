from fastapi import FastAPI
import subprocess

app = FastAPI()

def safe_ping(host):
    # Use subprocess.run instead and avoid shell=True
    try:
        result = subprocess.run(['ping', host], capture_output=True, text=True, check=True)
        return result.stdout
    except subprocess.CalledProcessError as e:
        return str(e)

def safe_ping_path(host):
    # Ensure the host parameter is sanitized to avoid directory traversal attacks
    import re
    if not re.match(r'^[a-zA-Z0-9.-]+$', host):
        raise ValueError('Invalid host name')
    return safe_ping(host)

@app.get("/ping")
def ping(host: str):
    return {'status': 'completed', 'output': safe_ping_path(host)}