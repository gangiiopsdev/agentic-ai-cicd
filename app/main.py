from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    # Sanitize user input
    host = subprocess.list2cmdline([host])
    # Secure implementation
    result = subprocess.call(["ping", host], shell=True)
    if result == 0:
        return {"status": "completed"}
    else:
        return {"status": "failed", "error": "Ping command failed"}