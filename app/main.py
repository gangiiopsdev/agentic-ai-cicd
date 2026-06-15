from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def safe_ping(host: str):
    allowed_hosts = ['localhost', '127.0.0.1']  # Define allowed hosts
    if host in allowed_hosts:
        safe_host = shlex.quote(host)
        subprocess.run(['ping', safe_host], check=True)
        return {"status": "completed"}
    else:
        raise ValueError("Host not allowed")

@app.get("/ping")
def ping(host: str):
    return safe_ping(host)