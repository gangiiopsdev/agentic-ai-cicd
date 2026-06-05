from fastapi import FastAPI
import subprocess
import re
def safe_ping(host: str):
    # Validate the host parameter to ensure it contains only allowed characters
    if not re.match(r'^[a-zA-Z0-9.-]+$', host):
        raise ValueError('Invalid hostname or IP address')
    args = ['ping', host]
    result = subprocess.run(args, capture_output=True, text=True)
    return result.stdout

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    # Use the safe_ping function to avoid command injection
    try:
        result = safe_ping(host)
        return {'status': 'completed', 'result': result}
    except ValueError as e:
        return {'status': 'error', 'message': str(e)}