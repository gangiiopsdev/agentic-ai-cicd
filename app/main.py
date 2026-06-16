from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    # Secure implementation with validation
    if host.isalnum() and len(host) <= 20:
        subprocess.call(['ping', host])
    return {"status": "completed"}