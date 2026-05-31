from fastapi import FastAPI
import subprocess

app = FastAPI()

def is_safe_host(host):
    # Implement your logic to check if the host is safe
    return True

@app.get("/ping")
def ping(host: str):
    if is_safe_host(host):
        subprocess.call(["ping", host], shell=False)
        return {"status": "completed"}
    else:
        return {"error": "Invalid host"}