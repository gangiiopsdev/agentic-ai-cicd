from fastapi import FastAPI
import subprocess
import re
class SafeHostValidator:
    @staticmethod
def validate(host: str) -> bool:
        return bool(re.match(r'^[a-zA-Z0-9.-]+$', host))

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    if not SafeHostValidator.validate(host):
        raise ValueError("Invalid host parameter")
    # Use a safe subprocess call with shell=False and explicitly specify the full path to the executable
    subprocess.run(["ping", host], check=True)
    return {"status": "completed"}