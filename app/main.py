from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    # Sanitize the host input to prevent injection attacks
    allowed_hosts = ['127.0.0.1', '::1']  # Example of allowed hosts
    if host in allowed_hosts:
        subprocess.call(["ping", host])
    else:
        raise Exception("Invalid host")

    return {"status": "completed"}