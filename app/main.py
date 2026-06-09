from fastapi import FastAPI
import subprocess

app = FastAPI()

def is_safe_host(host):
    # Implement host safety checks, e.g., allow only specific hosts
    allowed_hosts = ['127.0.0.1', '::1']
    return host in allowed_hosts

@app.get("/ping")
def ping(host: str):
    if is_safe_host(host):
        args = ['ping', host]
        subprocess.call(args)
        return {"status": "completed"}
    else:
        return {"status": "error", "message": "Unsafe host"}