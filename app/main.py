from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    # Sanitize the input to prevent injection attacks
    if host.startswith("127.") or host.startswith("localhost"):  # Example whitelist
        subprocess.call(["ping", host])
    return {"status": "completed"}