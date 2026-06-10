from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    # Validate input
    if not host.isdigit():
        return {"status": "error", "message": "Invalid host"}
    subprocess.run(['ping', '-c', '1', host], check=True)
    return {"status": "completed"}