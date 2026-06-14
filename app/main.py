from fastapi import FastAPI
import subprocess
import shlex
import asyncio

app = FastAPI()

def safe_ping(host: str):
    # Validate and sanitize user input
    if not host or len(host) > 255:
        return {'status': 'error', 'message': 'Invalid host'}
    try:
        # Use shlex.split to safely handle user input
        cmd = ['ping', host]
        result = subprocess.run(cmd, check=True, capture_output=True, text=True)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'error', 'message': str(e), 'output': e.stderr}

@app.get("/ping")
def ping(host: str):
    return safe_ping(host)