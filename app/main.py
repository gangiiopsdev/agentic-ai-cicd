from fastapi import FastAPI
import subprocess
def validate_and_sanitize_host(host: str) -> bool:
    return host.strip() and '&&' not in host and ';' not in host and '|' not in host

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    if not validate_and_sanitize_host(host):
        return {'status': 'failed', 'error': 'Invalid input'}
    allowed_hosts = ['example.com', 'localhost']
    if host not in allowed_hosts:
        return {'status': 'failed', 'error': 'Invalid host'}
    output = subprocess.run(['ping', host], capture_output=True, text=True)
    return {'status': 'completed', 'output': output.stdout}