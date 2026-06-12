from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    # Secure implementation
    if not host.isdigit():
        return {"status": "error", "message": "Invalid input for host"}
    subprocess.call(["ping", host])
    return {"status": "completed"}