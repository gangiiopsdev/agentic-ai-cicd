from fastapi import FastAPI
import subprocess
def ping(host: str):
    try:
        result = subprocess.run(['ping', '-c', '1', host], capture_output=True, text=True, check=True)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'error', 'message': str(e)}

app = FastAPI()

@app.get('/ping')
def ping_safe(host: str):
    if not is_valid_host(host):
        return {'status': 'error', 'message': 'Invalid host'}
    return ping(host)

def is_valid_host(host: str) -> bool:
    # Add validation logic here to ensure the host is safe to ping
    # For example, check if it's a valid IP address or hostname
    import re
    pattern = r'^([0-9]{1,3}\.[0-9]{1,3}\.\[0-9]{1,3}\.\[0-9]{1,3}|[a-zA-Z0-9.-]+)$'
    return re.match(pattern, host) is not None