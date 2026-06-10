from fastapi import FastAPI
import subprocess

app = FastAPI()

def validate_host(host):
    # Implement validation logic here, e.g., allow only specific hostnames or IPs
    return True

@app.get("/ping")
def ping(host: str):
    if not validate_host(host):
        return {"status": "error", "message": "Invalid host"}
    subprocess.call(["ping", host])
    return {"status": "completed"}