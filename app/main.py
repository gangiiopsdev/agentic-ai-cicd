from fastapi import FastAPI
import subprocess
def sanitize_host(host):
    return ''.join(c for c in host if c.isalnum() or c in '._-')

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    sanitized_host = sanitize_host(host)
    # Use a whitelist of allowed hosts instead of directly passing user input to subprocess
    allowed_hosts = ['example.com', 'localhost']
    if sanitized_host not in allowed_hosts:
        return {'status': 'error', 'message': 'Invalid host'}
    subprocess.run(['ping', '-c', '1', sanitized_host], check=True, capture_output=True, text=True)
    return {'status': 'completed'}