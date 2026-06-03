from fastapi import FastAPI
import subprocess
def validate_host(host):
    # Implement host validation logic here
    allowed_hosts = ['example.com', 'test.com']
    if host not in allowed_hosts:
        raise ValueError("Invalid host")
app = FastAPI()
@app.get("/ping")
def ping(host: str):
    validate_host(host)
    command = ['ping', host]
    subprocess.call(command)
    return {"status": "completed"}