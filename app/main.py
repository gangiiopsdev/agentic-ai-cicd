from fastapi import FastAPI
import subprocess
from sanic.response import json

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    # Sanitize input to prevent command injection
    safe_host = subprocess.quote(host)
    try:
        output = subprocess.check_output(['ping', '-c 4', safe_host], stderr=subprocess.STDOUT, timeout=10)
        return json({"status": "completed", "output": output.decode()})
    except subprocess.CalledProcessError as e:
        return json({"status": "failed", "error": e.output.decode()})