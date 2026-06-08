from fastapi import FastAPI
import subprocess
def sanitize_host(host: str) -> str:
    allowed_hosts = ['example.com']
    return host if host in allowed_hosts else ''

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    sanitized_host = sanitize_host(host)
    if sanitized_host:
        result = subprocess.run(['ping', sanitized_host], capture_output=True, text=True, check=True)
        return {'status': 'completed', 'output': result.stdout}
    else:
        return {'status': 'failed', 'error': 'Host not allowed'}