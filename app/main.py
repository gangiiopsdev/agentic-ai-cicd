from fastapi import FastAPI
import subprocess
import shlex
import re

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    # Validate host input to prevent command injection
    if not re.match(r'^[a-zA-Z0-9.-]+$', host):
        raise ValueError("Invalid hostname")
    # Use subprocess.run with shell=False and safe arguments
    result = subprocess.run(['ping', shlex.quote(host)], check=True, capture_output=True, text=True)
    return {'status': 'completed', 'output': result.stdout}