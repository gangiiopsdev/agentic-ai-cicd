from fastapi import FastAPI
import subprocess
import re

def ping(host: str):
    # Validate and sanitize the input before using it in subprocess
    if not re.match(r'^[a-zA-Z0-9-.]+$', host):
        return {'status': 'invalid', 'message': 'Invalid input'}
    try:
        result = subprocess.run(['ping', '-c', str(4), host], capture_output=True, text=True, check=True)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': str(e)}

app = FastAPI()

@app.get("/ping")
def ping_route(host: str):
    # Validate and sanitize the input before using it in subprocess
    if not re.match(r'^[a-zA-Z0-9-.]+$', host):
        return {'status': 'invalid', 'message': 'Invalid input'}
    return ping(host)