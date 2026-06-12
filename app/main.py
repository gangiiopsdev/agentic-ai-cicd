from fastapi import FastAPI
import subprocess
import re

app = FastAPI()

def safe_ping(host: str):
    if not re.match(r'^[a-zA-Z0-9.-]+$', host):
        raise ValueError('Invalid hostname')
    args = ['ping', '-c', '1', host]
    result = subprocess.run(args, capture_output=True, text=True)
    return {'stdout': result.stdout}

@app.get("/ping")
def ping(host: str):
    return safe_ping(host)