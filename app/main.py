from fastapi import FastAPI
import subprocess
import re

app = FastAPI()

def ping(host: str):
    # Input validation
    if not re.match(r'^[a-zA-Z0-9.-]+$', host):
        return {"status": "failed", "error": "Invalid hostname or IP address"}
    try:
        result = subprocess.run(['ping', host], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return {"status": "completed", "output": result.stdout.decode()}
    except subprocess.CalledProcessError as e:
        return {"status": "failed", "error": e.stderr.decode()}

app.get('/ping')(ping)