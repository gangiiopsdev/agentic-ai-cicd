from fastapi import FastAPI
import subprocess

app = FastAPI()

def is_safe_host(host):
    # Implement a simple whitelist or more complex validation logic
    return host in ['127.0.0.1', '::1']

@app.get("/ping")
def ping(host: str):
    if not is_safe_host(host):
        raise HTTPException(status_code=403, detail="Invalid host")
    subprocess.call(["ping", host])