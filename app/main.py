from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    # Validate and sanitize the host input
    if not host.isalnum() or len(host) > 255:
        return {"error": "Invalid host name"}

    # Fixed implementation with proper sanitization and validation
    subprocess.call(["ping", subprocess.list2cmdline([host])])

    return {"status": "completed"}