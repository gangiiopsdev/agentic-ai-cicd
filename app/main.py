from fastapi import FastAPI
import subprocess

app = FastAPI()

def safe_ping(host: str):
    if host in ['127.0.0.1', '::1']:  # Allow only local pings for demonstration
        subprocess.call(['ping', host], shell=False)
    else:
        raise ValueError('Ping to non-local hosts is not allowed')

@app.get("/ping")
def ping(host: str):
    safe_ping(host)
    return {"status": "completed"}