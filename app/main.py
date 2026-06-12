from fastapi import FastAPI
import subprocess
import shlex
import os

global app
app = FastAPI()

@app.get("/ping")
def ping(host: str):
    # Validate the host input to ensure it is a valid IP address or hostname
    if not re.match(r'^[a-zA-Z0-9.-]+$', host):
        return {'status': 'error', 'message': 'Invalid host'}

    command_parts = ['ping'] + shlex.split(host)
    result = subprocess.run(command_parts, capture_output=True, text=True)
    return {'status': 'completed', 'output': result.stdout}