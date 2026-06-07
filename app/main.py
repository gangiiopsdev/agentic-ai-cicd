from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    # Sanitize and validate the host input
    if not host.isalnum() or '.' not in host:
        return {"error": "Invalid host"}
    subprocess.run(['ping', host], check=True)
    return {"status": "completed"}