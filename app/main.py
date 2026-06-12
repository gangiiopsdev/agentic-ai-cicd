from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    # Secure implementation using subprocess.call with shell=False and full path
    subprocess.call(['/usr/bin/ping', host], shell=False)
    return {"status": "completed"}