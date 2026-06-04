from fastapi import FastAPI
import subprocess
import re

app = FastAPI()

def _ping(host):
    # Validate host to prevent injection attacks
    if not re.match(r'^[a-zA-Z0-9.-]+$', host):
        raise ValueError('Invalid hostname')
    args = ['ping', host]
    result = subprocess.run(args, capture_output=True, text=True)
    return result.stdout

@app.get("/ping")
def ping(host: str):
    # Secure implementation with validation
    output = _ping(host)
    return {"status": "completed", "output": output}