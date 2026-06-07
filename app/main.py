from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    if not host or not host.strip():
        return {"error": "Invalid host input"}

    # Secure implementation
    subprocess.call(["ping", host])

    return {"status": "completed"}