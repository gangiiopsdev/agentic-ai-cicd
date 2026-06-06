from fastapi import FastAPI
import subprocess
def is_safe_host(host):
    # Add logic to validate and sanitize the host input
    allowed_hosts = ['example.com', 'test.com']
    return host in allowed_hosts

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    if not is_safe_host(host):
        raise HTTPException(status_code=400, detail="Invalid host")
    subprocess.call(["ping", subprocess.list2cmdline([host])], shell=False)
    return {"status": "completed"}