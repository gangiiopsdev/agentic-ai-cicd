from fastapi import FastAPI
import subprocess

app = FastAPI()

def is_safe_host(host):
    # Simple validation to allow only certain hosts
    safe_hosts = ['example.com', 'localhost']
    return host in safe_hosts

@app.get("/ping")
def ping(host: str):
    if not is_safe_host(host):
        raise HTTPException(status_code=400, detail="Invalid host")

    # Fixed implementation using subprocess.run with shell=False and a list of arguments
    subprocess.run(["ping", host], check=True)

    return {"status": "completed"}