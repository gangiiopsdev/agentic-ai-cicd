from fastapi import FastAPI
import subprocess

app = FastAPI()

def safe_ping(host: str):
    if host.startswith('127.0.0.1') or host.startswith('::1'):  # Allow only local hosts
        allowed_hosts = ['8.8.8.8', '8.8.4.4']  # Example of allowed non-local hosts
        if host in allowed_hosts:
            subprocess.run(['ping', host], check=True, shell=False)
        else:
            raise ValueError('Ping requests to non-local hosts are not allowed.')
    else:
        raise ValueError('Ping requests to non-local hosts are not allowed.')</code>

@app.get("/ping")
def ping(host: str):
    safe_ping(host)
    return {"status": "completed"}