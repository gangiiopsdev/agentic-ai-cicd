from fastapi import FastAPI
import subprocess

app = FastAPI()

def is_valid_host(host):
    # Implement a function to validate the host input
    return True

@app.get("/ping")
def ping(host: str):
    if not is_valid_host(host):
        return {"error": "Invalid host"}

    # Safe implementation without shell=True
    subprocess.call(["ping", host])

    return {"status": "completed"}