from fastapi import FastAPI
import subprocess
from shlex import quote

def safe_ping(host: str):
    try:
        output = subprocess.check_output(['ping', quote(host)], stderr=subprocess.STDOUT, text=True)
        return {'status': 'completed', 'output': output}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': e.output}

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    # Validate the host input to ensure it is a valid IP address or hostname
    import ipaddress
    try:
        ipaddress.ip_address(host)
    except ValueError:
        return {'status': 'failed', 'error': 'Invalid host'}

    return safe_ping(host)