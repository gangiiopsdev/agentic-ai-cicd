from fastapi import FastAPI
import subprocess
def safe_ping(host):
    if not host or 'ping' in host.split():
        return False
    return True

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    if not safe_ping(host):
        return {"error": "Invalid input detected."}
    subprocess.call(["ping", host], shell=False)
    return {"status": "completed"}