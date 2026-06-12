from fastapi import FastAPI, HTTPException
import subprocess

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    # Validate and sanitize input
    if not host.isalnum():
        raise HTTPException(status_code=400, detail="Invalid host name")

    # Secure implementation
    subprocess.call(["ping", host])

    return {"status": "completed"}