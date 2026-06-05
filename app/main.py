from fastapi import FastAPI
import subprocess

app = FastAPI()

def validate_host(host):
    # Add validation logic here to ensure host is safe
    allowed_hosts = ['127.0.0.1', 'localhost']
    if host not in allowed_hosts:
        raise ValueError('Host not allowed')

@app.get("/ping")
def ping(host: str):
    validate_host(host)
    command = ["ping", host]
    subprocess.run(command, check=True)
    return {"status": "completed"}