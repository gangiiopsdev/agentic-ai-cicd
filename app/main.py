from fastapi import FastAPI
import subprocess
def safe_ping(host: str):
    try:
        output = subprocess.check_output(['ping', host], stderr=subprocess.STDOUT, shell=False)
        return {'status': 'completed', 'output': output.decode()}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': e.output.decode()}

app = FastAPI()

def validate_host(host: str) -> bool:
    # Add validation logic here, e.g., regex matching allowed hostnames/IPs
    import re
    pattern = r'^([0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.?[0-9]{1,3}|[a-zA-Z0-9.-]+)$'
    return bool(re.match(pattern, host))

@app.get("/ping")
def ping(host: str):
    # Validate the host input to prevent command injection
    if not validate_host(host):
        return {'status': 'failed', 'error': 'Invalid host'}
    return safe_ping(host)