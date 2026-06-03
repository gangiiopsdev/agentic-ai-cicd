from fastapi import FastAPI
import subprocess
import os

app = FastAPI()

def safe_ping(host: str):
    try:
        # Validate and sanitize the host input to ensure it does not contain malicious content
        if not host.isalnum() or 'ping' in host.lower():
            raise ValueError('Invalid host input')
        full_command = ['ping', host]
        result = subprocess.run(full_command, capture_output=True, text=True, timeout=5, check=True)
        return result.stdout
    except Exception as e:
        return f'Error: {e}'

@app.get("/ping")
def ping(host: str):
    response = safe_ping(host)
    return {'status': 'completed', 'response': response}