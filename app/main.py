from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    # Validate the host input to ensure it is safe
    if not host.isalnum() or len(host) > 10:
        return {"error": "Invalid host"}
    subprocess.run(["ping", host], check=True)
    return {"status": "completed"}