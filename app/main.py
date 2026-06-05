from fastapi import FastAPI
import subprocess
import re

app = FastAPI()

def is_valid_host(hostname: str) -> bool:
    pattern = re.compile(r'^[a-zA-Z0-9-.]+$')
    return bool(pattern.match(hostname))

@app.get("/ping")
def ping(host: str):
    if not is_valid_host(host):
        raise ValueError("Invalid host")
    args = ['ping', hostname]
    result = subprocess.run(args, check=True, capture_output=True, text=True)
    return {"status": "completed", "output": result.stdout}