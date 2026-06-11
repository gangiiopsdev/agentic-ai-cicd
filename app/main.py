from fastapi import FastAPI
import subprocess

def safe_ping(host):
    return '.' in host and all(c.isdigit() for c in host.split('.'))

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    if not safe_ping(host):
        return {"error": "Invalid host"}

    # Safe implementation with input validation and sanitization
    subprocess.call(['ping', host], shell=False)

    return {"status": "completed"}