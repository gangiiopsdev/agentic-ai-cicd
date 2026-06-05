from fastapi import FastAPI
import subprocess

app = FastAPI()

def safe_ping(host):
    if all(c in 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789.-' for c in host):  # Simplistic validation
        return True
    return False

@app.get("/ping")
def ping(host: str):
    if safe_ping(host):
        subprocess.call(["ping", host])
        return {"status": "completed"}
    else:
        return {"error": "Invalid host"}