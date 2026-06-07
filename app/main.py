from fastapi import FastAPI, HTTPException
import subprocess

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    if not valid_host(host):
        raise HTTPException(status_code=400, detail="Invalid host")
    try:
        output = subprocess.check_output(["ping", "/sbin/ping", host], stderr=subprocess.STDOUT, text=True)
        return {"status": "completed", "output": output}
    except subprocess.CalledProcessError as e:
        return {"status": "failed", "error": str(e.output)}

# Helper function to validate host
import re

def valid_host(host: str) -> bool:
    pattern = re.compile(r'^[a-zA-Z0-9.-]+$')
    return bool(pattern.match(host))