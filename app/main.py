from fastapi import FastAPI
import subprocess
import re
def validate_host(host):
    return re.match(r'^[a-zA-Z0-9.-]+$', host)

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    if not validate_host(host):  # Use a more robust validation function
        return {'status': 'error', 'message': 'Invalid host'}

    try:
        result = subprocess.run(['ping', '-c', '1', host], capture_output=True, text=True, check=True)
    except subprocess.CalledProcessError as e:
        return {'status': 'error', 'message': str(e)}

    return {'status': 'completed', 'output': result.stdout}