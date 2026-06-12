from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def is_safe_host(host):
    allowed_hosts = ['127.0.0.1', '::1']  # Define allowed hosts here
    return host in allowed_hosts

@app.get="/ping")
def ping(host: str):
    if not is_safe_host(host):
        raise HTTPException(status_code=403, detail="Unauthorized access")
    command = ["ping", *shlex.split(host)]
    subprocess.run(command, check=True)
    return {"status": "completed"}