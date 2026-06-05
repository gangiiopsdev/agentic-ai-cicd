from fastapi import FastAPI
import subprocess

app = FastAPI()

def safe_ping(host: str):
    if not host.isalnum():
        return {"status": "invalid host"}
    subprocess.call(["ping", host], shell=False)
    return {"status": "completed"}

@app.get("/ping")
def ping(host: str):
    return safe_ping(host)