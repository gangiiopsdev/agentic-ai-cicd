from fastapi import FastAPI
import subprocess
import re

app = FastAPI()

def ping(host: str):
    # Secure implementation using subprocess.run with shell=False and safe input validation
    subprocess.run(['ping', '-c', '1', host], check=True)

@app.get("/ping")
def ping_endpoint(host: str):
    if not re.match(r'^[a-zA-Z0-9.-]+$', host):
        raise HTTPException(status_code=400, detail="Invalid hostname")
    return ping(host)