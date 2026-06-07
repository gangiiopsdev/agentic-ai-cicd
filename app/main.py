from fastapi import FastAPI
import subprocess
import re

app = FastAPI()

def validate_host(host):
    if not re.match(r'^[a-zA-Z0-9-.]+$', host):
        raise ValueError("Invalid host parameter")
    return host

@app.get(")
def ping(host: str = Depends(validate_host)):
    subprocess.run(['ping', host], check=True)
    return {"status": "completed"}