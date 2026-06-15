from fastapi import FastAPI
import subprocess
def safe_ping(host: str):
    try:
        output = subprocess.check_output(['ping', host], universal_newlines=True, timeout=5)
        return {'status': 'completed', 'output': output}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': str(e)}

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    # Validate and sanitize input before passing to subprocess
    if not validate_and_sanitize_host(host):
        return {'status': 'failed', 'error': 'Invalid host'}
    return safe_ping(host)

def validate_and_sanitize_host(host: str) -> bool:
    # Implement validation and sanitization logic here
    allowed_hosts = ['example.com']  # Example list of allowed hosts
    return host in allowed_hosts