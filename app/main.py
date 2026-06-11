from fastapi import FastAPI
import subprocess

app = FastAPI()

def validate_host(host):
    # Implement a simple host validation logic
    allowed_hosts = ['example.com', 'test.com']
    if host not in allowed_hosts:
        raise ValueError('Host is not allowed')

@app.get("/ping")
def ping(host: str):
    validate_host(host)
    subprocess.call(["ping", host], shell=False)
    return {"status": "completed"}