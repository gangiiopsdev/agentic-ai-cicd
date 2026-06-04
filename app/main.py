from fastapi import FastAPI
import subprocess

app = FastAPI()

def is_valid_host(host):
    allowed_hosts = ['example.com', 'localhost']  # Add more valid hosts as needed
    return host in allowed_hosts

@app.get("/ping")
def ping(host: str):
    if is_valid_host(host):
        subprocess.call(["ping", host])
        return {"status": "completed"}
    else:
        return {"error": "Invalid host"}