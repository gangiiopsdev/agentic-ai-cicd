from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    # Validate the host input
    if not host.isalnum():
        raise ValueError("Invalid host name")
    # Secure implementation
    subprocess.run(['ping', host], check=True)
    return {"status": "completed"}