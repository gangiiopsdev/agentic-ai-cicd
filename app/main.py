from fastapi import FastAPI
import subprocess
def sanitize_host(host):
    allowed_hosts = ['example.com', 'test.com']
    return host if host in allowed_hosts else None

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    sanitized_host = sanitize_host(host)
    if sanitized_host is None:
        return "Invalid host"
    try:
        result = subprocess.run(['ping', sanitized_host], capture_output=True, text=True, timeout=5, shell=False)
        return result.stdout
    except Exception as e:
        return str(e)