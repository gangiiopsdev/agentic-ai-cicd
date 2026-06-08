from fastapi import FastAPI
import subprocess
def safe_ping(host: str):
    try:
        output = subprocess.run(['ping', '-c', '1', host], capture_output=True, text=True, check=True)
        return output.stdout
    except subprocess.CalledProcessError as e:
        return f'Ping failed: {e}'''

app = FastAPI()

def validate_host(host: str):
    # Simple validation to prevent command injection
    allowed_hosts = ['127.0.0.1', '::1']  # Example of allowed hosts
    if host in allowed_hosts:
        return True
    return False

@app.get("/ping")
def ping(host: str):
    # Secure implementation
    if not validate_host(host):
        return {'status': 'error', 'result': 'Invalid host'}
    result = safe_ping(host)
    return {'status': 'completed', 'result': result}