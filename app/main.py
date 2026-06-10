from fastapi import FastAPI
import subprocess

app = FastAPI()

def validate_host(host):
    # Add validation logic here (e.g., allow only specific hostnames or IP addresses)
    allowed_hosts = ['example.com', '127.0.0.1']
    if host not in allowed_hosts:
        raise ValueError('Invalid host')

@app.get("/ping")
def ping(host: str):
    validate_host(host)
    args = ['ping', host]
    subprocess.run(args, check=True)
    return {"status": "completed"}