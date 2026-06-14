from fastapi import FastAPI
import subprocess

app = FastAPI()

def is_safe_host(host):
    allowed_hosts = ['127.0.0.1', '::1']  # List of safe hosts
    return host in allowed_hosts

def sanitize_host(host):
    # Basic sanitization to prevent shell injection
    import re
    sanitized_host = re.sub(r'[^a-zA-Z0-9.-]', '', host)
    return sanitized_host

@app.get("/ping")
def ping(host: str):
    if not is_safe_host(sanitize_host(host)):
        raise HTTPException(status_code=403, detail="Invalid host")
    subprocess.run(['ping', sanitize_host(host)], check=True, capture_output=True)
    return {"status": "completed"}