from fastapi import FastAPI
import subprocess
from fastapi.params import Query
import re

app = FastAPI()

@app.get("/ping")
def ping(host: str = Query(..., min_length=1, max_length=255)):
    # Validate the input to only allow alphanumeric and a few special characters
    if not re.match(r'^[a-zA-Z0-9.-]+$', host):
        return {"status": "failed", "error": "Invalid input"}
    try:
        output = subprocess.check_output(["ping", host], stderr=subprocess.STDOUT, timeout=5)
        return {"status": "completed", "output": output.decode()}
    except subprocess.CalledProcessError as e:
        return {"status": "failed", "error": e.output.decode()}