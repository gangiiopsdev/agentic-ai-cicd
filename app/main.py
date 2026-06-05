from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    # Validate and sanitize input
    if host.strip() == '':
        return {"status": "failed", "message": "Host is empty"}
    subprocess.call(["ping", host])
    return {"status": "completed"}