from fastapi import FastAPI
import subprocess

app = FastAPI()

def safe_ping(host: str):
    # Validate and sanitize host input
    if not host.isalnum() or len(host) > 255:
        return False, "Invalid host name"
    try:
        output = subprocess.check_output(['ping', '-c', '1', host], stderr=subprocess.STDOUT, text=True)
        return True, output
    except subprocess.CalledProcessError as e:
        return False, str(e)

def ping(host: str):
    success, result = safe_ping(host)
    if not success:
        return {'status': 'failed', 'error': result}
    return {'status': 'completed', 'output': result}