from fastapi import FastAPI
import subprocess
def safe_ping(host):
    try:
        output = subprocess.check_output(['ping', host], timeout=1, stderr=subprocess.STDOUT)
        return {'status': 'completed', 'output': output.decode('utf-8')}
    except (subprocess.CalledProcessError, subprocess.TimeoutExpired) as e:
        return {'status': 'failed', 'error': str(e)}

app = FastAPI()
@app.get("/ping")
def ping(host: str):
    # Validate the host to prevent command injection
    if not is_valid_host(host):
        return {'status': 'failed', 'error': 'Invalid host'}
    return safe_ping(host)

def is_valid_host(host):
    # Implement validation logic here, e.g., regex pattern matching for allowed hosts
    import re
    return re.match(r'^[a-zA-Z0-9.-]+$', host) is not None