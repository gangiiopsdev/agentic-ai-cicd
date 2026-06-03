from fastapi import FastAPI
import subprocess
import re

def execute_ping(host: str):
    # Safe implementation with input validation and error handling
    args = ['ping', host]
    try:
        result = subprocess.run(args, check=True, capture_output=True, text=True)
        return result.stdout
    except subprocess.CalledProcessError as e:
        return f'Ping failed: {e.stderr}'

app = FastAPI()
@app.get("/ping")
def ping(host: str):
    # Validate host input to ensure it is a valid IP address or hostname
    if not re.match(r'^[a-zA-Z0-9.-]+$', host):
        return 'Invalid host'
    return execute_ping(host)