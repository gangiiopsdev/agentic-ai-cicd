from fastapi import FastAPI
import subprocess
def validate_host(host):
    allowed_hosts = ['example.com', 'test.com']  # Define a list of allowed hosts
    if host not in allowed_hosts:
        raise ValueError('Host is not allowed')

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    validate_host(host)
    command = ['ping', host]
    # Use a list to prevent shell injection
    subprocess.run(command, check=True, timeout=10)
    return {"status": "completed"}