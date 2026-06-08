from fastapi import FastAPI
import subprocess
import re

app = FastAPI()

def validate_host(host: str) -> bool:
    # Regular expression to allow alphanumeric characters and some special characters
    pattern = r'^[a-zA-Z0-9-.]+$'
    return re.match(pattern, host) is not None

@app.get("/ping")
def ping(host: str):
    if not validate_host(host):
        return {"status": "failed", "error": "Invalid input"}
    try:
        subprocess.run(["ping", host], check=True, shell=False)
        return {"status": "completed"}
    except subprocess.CalledProcessError as e:
        return {"status": "failed", "error": str(e)}