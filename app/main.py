from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    allowed_hosts = ["example.com", "test.com"]  # Replace with actual allowed hosts
    if host not in allowed_hosts:
        return {"status": "error", "message": "Host not allowed"}
    subprocess.call(["ping", host], shell=False)
    return {"status": "completed"}