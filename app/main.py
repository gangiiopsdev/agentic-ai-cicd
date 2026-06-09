from fastapi import FastAPI
import subprocess
import re

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    # Validate the host input to ensure it does not contain malicious characters
    if not re.match(r'^[a-zA-Z0-9.-]+$', host):
        return {'status': 'error', 'message': 'Invalid host'}
    args = ['ping', host]
    result = subprocess.run(args, capture_output=True, text=True, check=False)
    if result.returncode != 0:
        return {'status': 'error', 'message': 'Ping failed'}
    return {'status': 'completed'}