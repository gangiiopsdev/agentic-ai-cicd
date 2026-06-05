from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    if not host.isalnum():
        return {"status": "error", "message": "Invalid host name"}
    sanitized_host = subprocess.list2cmdline([host])
    subprocess.run(["ping", sanitized_host], check=True, shell=False)
    return {"status": "completed"}