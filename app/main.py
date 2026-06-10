from fastapi import FastAPI
import subprocess
def is_valid_host(host):
    # Basic validation for demonstration purposes
    return '.' in host

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    if not is_valid_host(host):
        return {'status': 'failed', 'error': 'Invalid host'}
    try:
        result = subprocess.run(['ping', host], capture_output=True, text=True, check=True, shell=False)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': str(e)}

# Additional validation to ensure the host is a valid IP address or hostname
import socket
def is_valid_host(host):
    try:
        socket.gethostbyname(host)
        return True
    except socket.gaierror:
        return False