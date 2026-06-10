from fastapi import FastAPI
import subprocess
from fastapi import HTTPException
def is_safe_host(host):
    safe_hosts = ['example.com', '127.0.0.1']
    if host in safe_hosts:
        return True
    raise HTTPException(status_code=403, detail="Unauthorized host")

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    if not is_safe_host(host):
        raise HTTPException(status_code=403, detail="Unauthorized host")

    # Secure implementation
    subprocess.run(['ping', host], check=True)

    return {"status": "completed"}