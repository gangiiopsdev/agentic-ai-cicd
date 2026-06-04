from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    if not host.isalnum():
        return {"status": "error", "message": "Invalid host name"}
    subprocess.run(["ping", host], check=True, shell=False)
    return {"status": "completed"}