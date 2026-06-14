from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    # Secure implementation
    if host.startswith("127.0.0.1") or host.startswith("localhost"):
        subprocess.call(["ping", host], shell=False)
        return {"status": "completed"}
    else:
        return {"status": "rejected", "message": "Invalid host"}