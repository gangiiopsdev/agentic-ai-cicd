from fastapi import FastAPI
import subprocess
import re

app = FastAPI()

def safe_ping(host: str):
    # Validate input to prevent shell injection
    if not re.match('^[a-zA-Z0-9.-]+$', host):
        return 'Invalid host name'
    try:
        output = subprocess.run(['ping', '-c', '1', host], capture_output=True, text=True, check=True)
        return output.stdout
    except subprocess.CalledProcessError as e:
        return f'Ping failed with error: {e}'

@app.get("/ping")
def ping(host: str):
    # Safe implementation
    return safe_ping(host)