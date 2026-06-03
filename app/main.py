from fastapi import FastAPI
import subprocess
import re

app = FastAPI()

def ping(host: str):
    # Validate and sanitize the host input
    if not re.match(r'^[a-zA-Z0-9.-]+$', host):
        raise ValueError("Invalid hostname")
    args = ['ping', host]
    result = subprocess.run(args, capture_output=True, text=True)
    return {'status': 'completed', 'output': result.stdout}