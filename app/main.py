from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    # Validate and sanitize host input
    if not all(c.isalnum() or c in ('.', '-') for c in host):
        return {"status": "error", "message": "Invalid host"}
    subprocess.call(["ping", host], shell=False)

    return {"status": "completed"}