from fastapi import FastAPI
import subprocess

app = FastAPI()

def safe_ping(host: str):
    if not all(c in 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789.-' for c in host):  # Simple validation
        return False
    subprocess.call(f"ping {host}", shell=False)

@app.get("/ping")
def ping(host: str):
    if safe_ping(host):
        return {"status": "completed"}
    else:
        return {"status": "Invalid host", "error": "Hostname contains invalid characters"}