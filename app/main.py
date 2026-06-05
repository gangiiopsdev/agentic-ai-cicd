from fastapi import FastAPI
import subprocess
import re

app = FastAPI()

async def is_valid_host(host: str):
    pattern = r'^[a-zA-Z0-9.-]+$'
    return re.match(pattern, host) is not None

def validate_and_escape_host(host: str):
    # Ensure the host does not contain any characters that could be used in a command injection attack
    if any(char in '&|;*?~<>^()[]{}$\`' for char in host):
        raise ValueError('Invalid host name')
    return subprocess.quote(host)

async def ping(host: str):
    escaped_host = validate_and_escape_host(host)
    result = await subprocess.run(['ping', '-c', '1', escaped_host], capture_output=True, text=True, check=True)
    return result.stdout

@app.get("/ping")
def ping_route(host: str):
    try:
        result = await ping(host)
        return {'status': 'completed', 'output': result}
    except subprocess.CalledProcessError as e:
        return {'status': 'error', 'message': str(e)}