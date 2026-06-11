from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    # Validate and sanitize the host input
    if not host or not host.strip():
        return {'error': 'Invalid host'}, 400

    # Fixed implementation
    subprocess.run(["ping", host], check=True)

    return {"status": "completed"}