from fastapi import FastAPI
import subprocess
import re

app = FastAPI()

def ping(host: str):
    # Validate input
    if not re.match(r'^[a-zA-Z0-9.-]+$', host):
        return {'status': 'failed', 'error': 'Invalid host'}
    
    # Sanitize input
    host = shlex.quote(host)
    result = subprocess.run(['ping', '-c', '4', host], capture_output=True, text=True, check=False)
    if result.returncode != 0:
        return {'status': 'failed', 'error': str(result.stderr)}
    else:
        return {'status': 'completed', 'output': result.stdout}

@app.get("/ping")
def ping_endpoint(host: str):
    return ping(host)