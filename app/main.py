from fastapi import FastAPI
import subprocess
def safe_ping(host: str):
    allowed_hosts = ['127.0.0.1', '::1']  # Define a whitelist of allowed hosts
    if host in allowed_hosts:
        command = ['ping', host]
        subprocess.run(command, check=True)
        return {"status": "completed"}
    else:
        raise ValueError("Host not allowed")

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    return safe_ping(host)