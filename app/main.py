from fastapi import FastAPI
import re
import subprocess

app = FastAPI()

def safe_ping(host: str):
    # Validate and sanitize the host input to prevent command injection
    if not re.match(r'^[a-zA-Z0-9]{1,255}$', host):
        return False, {'status': 'failed', 'error': 'Invalid host input'}
    try:
        result = subprocess.run(['ping', host], capture_output=True, text=True, check=True)
        return True, {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return False, {'status': 'failed', 'error': str(e)}

@app.get('/ping')
def ping(host: str):
    success, response = safe_ping(host)
    if success:
        return response
    else:
        return response