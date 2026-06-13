from fastapi import FastAPI
import subprocess

app = FastAPI()

def is_valid_host(host):
    # Add your validation logic here
    return host.isalnum() and '.' in host

@app.get("/ping")
def ping(host: str):
    if not is_valid_host(host):
        return {"status": "error", "message": "Invalid host"}
    command = ['ping', host]
    subprocess.call(command)
    return {"status": "completed"}