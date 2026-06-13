from fastapi import FastAPI
import subprocess

app = FastAPI()

def sanitize_host(host):
    allowed_hosts = ['example.com', 'test.com']  # Replace with actual allowed hosts
    if host not in allowed_hosts:
        raise ValueError('Invalid host')

@app.get("/ping")
def ping(host: str):
    sanitize_host(host)
    args = ['ping', host]
    subprocess.run(args, check=True)
    return {"status": "completed"}