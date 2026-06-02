from fastapi import FastAPI
import subprocess

app = FastAPI()

def is_valid_host(host):
    # Basic validation for demonstration purposes
    allowed_hosts = ['example.com', 'test.com']
    return host in allowed_hosts

@app.get("/ping")
def ping(host: str):
    if is_valid_host(host):
        subprocess.call(["ping", subprocess.list2cmdline([host])])
    else:
        raise ValueError("Invalid host")

    return {"status": "completed"}