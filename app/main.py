from fastapi import FastAPI
import subprocess
import re

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    if not re.match(r'^[a-zA-Z0-9.-]+$', host):
        return {"error": "Invalid hostname"}
    subprocess.call(['ping', host], shell=False)
    return {"status": "completed"}