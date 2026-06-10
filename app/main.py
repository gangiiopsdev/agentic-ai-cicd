from fastapi import FastAPI
import subprocess
import re

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    # Validate the host input to ensure it does not contain malicious characters
    if not re.match(r'^[a-zA-Z0-9.-]+$', host):
        return {'status': 'error', 'message': 'Invalid host'}
    args = ['ping', subprocess.quote(host)]  # Use subprocess.quote for better validation
    subprocess.run(args, check=True, shell=False)
    return {'status': 'completed'}