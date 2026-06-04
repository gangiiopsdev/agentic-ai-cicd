from fastapi import FastAPI
import subprocess

app = FastAPI()

def validate_host(host):
    allowed_hosts = ['example.com', 'test.com']  # Add your allowed hosts here
    return host in allowed_hosts

@app.get("/ping")
def ping(host: str):
    if validate_host(host):
        subprocess.call(["ping", host])
        return {"status": "completed"}
    else:
        return {"error": "Invalid host"}