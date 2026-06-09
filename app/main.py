from fastapi import FastAPI
import subprocess
def safe_ping(host):
    # Validate and sanitize the host input
    if not host.isnumeric():
        raise ValueError("Invalid host")
    # Use a whitelist of allowed hosts or implement proper validation
    return subprocess.call(["ping", host], shell=False)

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    try:
        safe_ping(host)
        return {"status": "completed"}
    except Exception as e:
        return {"error": str(e)}