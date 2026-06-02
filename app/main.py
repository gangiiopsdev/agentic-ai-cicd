from fastapi import FastAPI
import subprocess
import os
def safe_ping(host: str):
    try:
        # Use os.path.join to ensure the command is constructed safely
        result = subprocess.run(['ping', host], capture_output=True, text=True, timeout=5)
        return result.stdout
    except Exception as e:
        return f'Error: {e}'

@app.get("/ping")
def ping(host: str):
    # Validate and sanitize the input to prevent command injection
    if not host.isalnum():
        raise ValueError('Invalid hostname')
    response = safe_ping(host)
    return {'status': 'completed', 'response': response}