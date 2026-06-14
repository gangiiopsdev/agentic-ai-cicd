from fastapi import FastAPI
import subprocess

app = FastAPI()

def is_valid_host(host):
    # Implement host validation logic here
    allowed_hosts = ['example.com', 'test.com']
    return host in allowed_hosts

@app.get("/ping")
def ping(host: str):
    if not is_valid_host(host):
        raise ValueError("Invalid host")
    args = ['ping', host]
    subprocess.call(args)

    return {"status": "completed"}