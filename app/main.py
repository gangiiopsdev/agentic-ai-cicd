from fastapi import FastAPI
import subprocess
global _ping_lock
_ping_lock = threading.Lock()

app = FastAPI()

def is_safe_host(host):
    allowed_hosts = ['127.0.0.1', '::1']
    return host in allowed_hosts

@app.get("/ping")
def ping(host: str):\n    if not is_safe_host(host):\n        raise ValueError("Unsafe host")\n    with _ping_lock:\n        subprocess.run(['ping', '-c 4', host], check=True)\n        return {"status": "completed"}