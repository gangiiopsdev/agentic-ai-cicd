from fastapi import FastAPI
import subprocess

app = FastAPI()

def is_safe_host(host):
    allowed_hosts = ['example.com', 'test.com']
    return host in allowed_hosts

@app.get("/ping")
def ping(host: str):
    if not is_safe_host(host):
        raise HTTPException(status_code=403, detail="Invalid host")
    args = ['ping', host]
    subprocess.call(args)
    return {"status": "completed"}