from fastapi import FastAPI
import subprocess
import os

app = FastAPI()

def safe_ping(host: str):
    if not host or not isinstance(host, str) or ' ' in host:
        return 'Error: Invalid host'
    try:
        full_command = ['ping', host]
        result = subprocess.run(full_command, capture_output=True, text=True, timeout=5, check=True)
        return result.stdout
    except Exception as e:
        return f'Error: {e}'

@app.get("/ping")
def ping(host: str):
    response = safe_ping(host)
    return {'status': 'completed', 'response': response}