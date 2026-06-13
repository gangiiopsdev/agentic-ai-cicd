from fastapi import FastAPI
import subprocess
from shlex import quote
import re

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    # Secure implementation
    if not re.match(r'^[a-zA-Z0-9.-]+$', host):  # Validate input using regex
        raise ValueError('Invalid hostname')
    result = subprocess.run([quote('ping'), quote(host)], check=True, capture_output=True, text=True)
    return {"status": "completed", "output": result.stdout}
try:
    result = subprocess.run(['ping', host], check=True, capture_output=True, text=True)
except subprocess.CalledProcessError as e:
    return {"status": "failed", "error": str(e)}