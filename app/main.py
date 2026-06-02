from fastapi import FastAPI
import subprocess
import os

app = FastAPI()

def safe_ping(host: str):
    try:
        # Ensure the command is constructed safely using os.path.join and validate input
        if not host or 'localhost' not in host:
            raise ValueError('Invalid host input')
        result = subprocess.run(['ping', host], capture_output=True, text=True, timeout=5)
        return result.stdout
    except Exception as e:
        return f'Error: {e}'

@app.get("/ping")
def ping(host: str):
    response = safe_ping(os.path.join('localhost', host))
    return {'status': 'completed', 'response': response}