from fastapi import FastAPI
import subprocess
def sanitize_host(host):
    # Basic validation: Allow only alphanumeric characters and hyphens
    if all(c.isalnum() or c == '-' for c in host) and len(host) <= 64:
        return host
    raise ValueError('Invalid hostname')

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    sanitized_host = sanitize_host(host)
    try:
        subprocess.run(['ping', sanitized_host], check=True, timeout=5)
    except subprocess.CalledProcessError as e:
        return {"status": "failed", "error": str(e)}
    return {"status": "completed"}