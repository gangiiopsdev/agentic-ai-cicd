from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    # Validate the host parameter
    if not host.isalnum() or len(host) > 255:
        return {"status": "error", "message": "Invalid host"}
    subprocess.call(["ping", host])
    return {"status": "completed"}