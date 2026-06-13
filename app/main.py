from fastapi import FastAPI
import subprocess

app = FastAPI()

def sanitize_host(host):
    # Implement sanitization logic here (e.g., whitelist of allowed hosts)
    allowed_hosts = ['127.0.0.1']
    if host in allowed_hosts:
        return host
    else:
        raise ValueError('Invalid host')

@app.get("/ping")
def ping(host: str):
    sanitized_host = sanitize_host(host)
    subprocess.run(['ping', f'--', sanitized_host], check=True)
    return {"status": "completed"}