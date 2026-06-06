from fastapi import FastAPI
import subprocess

app = FastAPI()

def is_safe_host(host):
    # Add logic to check if the host is safe
    return True

@app.get("/ping")
def ping(host: str):
    if not is_safe_host(host):
        return {"status": "error", "message": "Invalid host"}
    subprocess.call(['ping', host], shell=False)
    return {"status": "completed"}