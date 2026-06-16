from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    # Validate and sanitize input
    if not host.isalnum() or len(host) > 255:
        return {"error": "Invalid host name"}, 400
    subprocess.run(['ping', host], check=True)
    return {"status": "completed"}