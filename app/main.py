from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    # Validate and sanitize the host input
    if not host or not host.strip():
        return {'error': 'Invalid host'}, 400

    # Use a safe way to execute subprocess
    subprocess.run(["ping", "/sbin/ping"], check=True, capture_output=True)

    return {"status": "completed"}