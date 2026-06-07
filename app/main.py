from fastapi import FastAPI
import subprocess

app = FastAPI()

def safe_ping(host: str):
    allowed_hosts = ['127.0.0.1', '::1']  # Define a list of allowed hosts
    if host in allowed_hosts:
        subprocess.run(["ping", host], check=True)
        return {"status": "completed"}
    else:
        return {'error': 'Host not allowed'}

@app.get("/ping")
def ping(host: str):
    return safe_ping(host)