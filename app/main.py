from fastapi import FastAPI
import subprocess
def safe_ping(host: str):
    if not host.isnumeric():
        return {'status': 'error', 'message': 'Invalid host'}
    # Sanitize input further if necessary
    result = subprocess.run(['ping', host], capture_output=True, text=True, check=True)
    return {'status': 'success', 'output': result.stdout}
app = FastAPI()
@app.get("/ping")
def ping(host: str):
    # Ensure the host is a valid IP address or hostname
    if not (host.startswith('192.168.') or host.isnumeric()):
        return {'status': 'error', 'message': 'Invalid host'}
    return safe_ping(host)