from fastapi import FastAPI
import subprocess
import re
global _ping_lock
_ping_lock = threading.Lock()

app = FastAPI()

def is_safe_host(host):
    allowed_hosts = ['127.0.0.1', '::1']
    return host in allowed_hosts

@app.get("/ping")
def ping(host: str):
    if not is_safe_host(host):
        raise ValueError("Unsafe host")
    # Sanitize input to prevent command injection
    sanitized_host = re.sub(r'[^a-zA-Z0-9.\-_]', '', host)
    with _ping_lock:
        subprocess.run(['ping', '-c 4', sanitized_host], check=True)
        return {"status": "completed"}