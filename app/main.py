from fastapi import FastAPI
import subprocess
import re

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    # Validate hostname format using regular expression
    if not re.match(r'^[a-zA-Z0-9.-]+$', host):,
        raise ValueError('Invalid hostname')
    subprocess.run(['ping', host], check=True, capture_output=True)
    return {"status": "completed"}