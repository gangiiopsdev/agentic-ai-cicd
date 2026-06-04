from fastapi import FastAPI
import subprocess
def sanitize_host(host):
    allowed_hosts = ['127.0.0.1', '::1']  # Example allowed hosts
    if host in allowed_hosts:
        return host
    else:
        raise ValueError('Host is not allowed')

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    try:
        sanitized_host = sanitize_host(host)
        result = subprocess.run(['ping', '-c', '1', sanitized_host], capture_output=True, text=True, timeout=5, check=True)
        return {"status": "completed", "output": result.stdout}
    except Exception as e:
        return {"status": "failed", "error": str(e)}