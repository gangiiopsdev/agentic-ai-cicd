from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    # Secure implementation
    if not host.isalnum():
        raise ValueError("Invalid host provided")
    subprocess.run(['ping', host], check=True)
    return {"status": "completed"}