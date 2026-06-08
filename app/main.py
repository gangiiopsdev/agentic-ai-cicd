from fastapi import FastAPI
import subprocess
import re

app = FastAPI()

def safe_ping(host: str):
    # Using subprocess.run with a list instead of a string for safety
    subprocess.run(['ping', host])

@app.get("/ping")
def ping(host: str):
    # Validate or sanitize the input to prevent command injection
    if not re.match(r'^[a-zA-Z0-9.-]+$', host):
        return {'error': 'Invalid input'}
    safe_ping(host)
    return {'message': f'Pinging {host}'}