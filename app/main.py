from fastapi import FastAPI
import subprocess

app = FastAPI()

def validate_host(host):
    # Implement a simple host validation logic
    allowed_hosts = ['example.com', 'another-example.com']
    return host in allowed_hosts

@app.get("/ping")
def ping(host: str):
    if validate_host(host):
        subprocess.run(["ping", host], check=True)
        return {"status": "completed"}
    else:
        return {"error": "Invalid host"}, 400