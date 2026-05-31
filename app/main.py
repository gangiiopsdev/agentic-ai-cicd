from fastapi import FastAPI
import subprocess
import re

app = FastAPI()

def ping(host: str):
    # Validate input to prevent command injection
    if not re.match(r'^[a-zA-Z0-9.-]+$', host):
        raise ValueError("Invalid host name")
    try:
        result = subprocess.run(['ping', host], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        return {'host': host, 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'host': host, 'error': str(e)}

@app.get("/ping")
def ping_endpoint(host: str):
    return ping(host)