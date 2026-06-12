from fastapi import FastAPI
import subprocess
def sanitize_host(host):
    allowed_hosts = ['example.com', 'localhost']
    if host not in allowed_hosts:
        return None
    return host

app = FastAPI()
@app.get("/ping")
def ping(host: str):
    sanitized_host = sanitize_host(host)
    if sanitized_host is None:
        return {'status': 'error', 'message': 'Unauthorized host'}
    result = subprocess.run(['ping', sanitized_host], capture_output=True, text=True)
    return {'status': 'completed', 'output': result.stdout}