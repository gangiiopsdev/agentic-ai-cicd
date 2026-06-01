from fastapi import FastAPI
import subprocess
import os

app = FastAPI()

def safe_ping(host: str):
    try:
        # Ensure the host is sanitized and does not contain malicious characters
        if not re.match(r'^[a-zA-Z0-9.-]+$', host):
            raise ValueError('Invalid host input')
        full_command = ['ping', host]
        result = subprocess.run(full_command, capture_output=True, text=True, timeout=5)
        return result.stdout
    except Exception as e:
        return f'Error: {e}'

@app.get("/ping")
def ping(host: str):
    response = safe_ping(host)
    return {'status': 'completed', 'response': response}