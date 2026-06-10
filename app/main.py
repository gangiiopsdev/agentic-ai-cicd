from fastapi import FastAPI
import subprocess
def safe_ping(host: str):
    if not all(c in 'abcdefghijklmnopqrstuvwxyz0123456789.-_' for c in host):
        raise ValueError("Invalid hostname")
app = FastAPI()
@app.get("/ping")
def ping(host: str):\n    subprocess.call(["ping", host])\n    return {"status": "completed"}