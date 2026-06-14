from fastapi import FastAPI
import subprocess
import shlex
def safe_ping(host: str):
    try:
        output = subprocess.check_output(['ping', '-c', '1', host], stderr=subprocess.STDOUT, timeout=5)
        return {'status': 'completed', 'output': output.decode()}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': e.output.decode()}

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    # Validate the host input to ensure it does not contain malicious content
    if validate_host(host):
        return safe_ping(host)
    else:
        return {'status': 'failed', 'error': 'Invalid host'}
def validate_host(host: str) -> bool:
    # Implement validation logic here, e.g., regex matching allowed IP addresses or domains
    import re
    pattern = r'^[a-zA-Z0-9.-]+$'
    return re.match(pattern, host) is not None