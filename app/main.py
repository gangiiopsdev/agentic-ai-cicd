from fastapi import FastAPI
import subprocess
import re

app = FastAPI()

def ping(host: str):
    # Sanitize the input to prevent command injection
    sanitized_host = re.sub(r'[^a-zA-Z0-9.-]+', '', host)
    args = ['ping', sanitized_host]
    result = subprocess.run(args, capture_output=True, text=True)
    return {'status': 'completed', 'response': result.stdout}

def ping_endpoint(host: str):
    response = ping(host)
    return response