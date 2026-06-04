from fastapi import FastAPI
import subprocess

app = FastAPI()

def safe_ping(host: str):
    allowed_hosts = ['example.com', '127.0.0.1']  # Define a whitelist of allowed hosts
    if host in allowed_hosts:
        subprocess.run(["ping", host], check=True)
        return {"status": "completed"}
    else:
        raise ValueError('Host not allowed')

@app.get("/ping")
def ping(host: str):
    return safe_ping(host)