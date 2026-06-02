from fastapi import FastAPI
import subprocess
import re

app = FastAPI()

def ping(host: str):
    # Validate the input to prevent command injection
    if not all(c.isalnum() or c in '-.' for c in host) or re.search(r'[^a-zA-Z0-9-.]', host):
        return {'status': 'error', 'message': 'Invalid host name'}
    try:
        output = subprocess.run(['ping', host], capture_output=True, text=True, check=True)
        return {'status': 'completed', 'output': output.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'error', 'message': str(e)}

@app.get("/ping")
def ping_endpoint(host: str):
    return ping(host)