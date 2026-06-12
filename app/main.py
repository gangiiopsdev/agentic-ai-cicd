from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def safe_ping(host: str):
    # Validate and sanitize the host input
    if any(char in host for char in '!@#$%^&*()_+{}|:"<>?/\`~=[];',):  # Basic check for special characters
        return {'error': 'Invalid host'}, 400
    command_parts = shlex.split(f'ping {host}')
    subprocess.call(command_parts)

@app.get('/ping')
def ping(host: str):
    response, status_code = safe_ping(host)
    return response