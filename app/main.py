from fastapi import FastAPI
import subprocess
import re

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    if not re.match(r'^[a-zA-Z0-9]{1,255}$', host):  # Regex to validate alphanumeric and length
        raise ValueError('Invalid host name')
    result = subprocess.run(['ping', host], capture_output=True, text=True, check=True)
    return {"status": "completed", "output": result.stdout}