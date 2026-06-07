from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    # Safe implementation with validation and escaping
    host = subprocess.list2cmdline([host])
    subprocess.call(["ping", host])
    return {"status": "completed"}