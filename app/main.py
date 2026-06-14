from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    # Safe implementation with input sanitization and use of shell=False
    if host.isalnum() and len(host) < 256:
        subprocess.call(["ping", host], shell=False)
        return {"status": "completed"}
    else:
        return {"error": "Invalid host name"}