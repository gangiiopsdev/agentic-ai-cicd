from fastapi import FastAPI
import subprocess
import re

app = FastAPI()

def validate_host(host: str):
    if re.match(r'^[a-zA-Z0-9.-]+$', host) is None:
        raise ValueError("Invalid hostname")

@app.get("/ping")
def ping(host: str):
    try:
        subprocess.run(["ping", host], check=True, shell=False)
        return {"status": "completed"}
    except subprocess.CalledProcessError as e:
        return {"status": "error", "message": str(e)}