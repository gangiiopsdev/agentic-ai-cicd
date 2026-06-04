from fastapi import FastAPI
import subprocess
import re

app = FastAPI()

def is_valid_host(host: str) -> bool:
    pattern = re.compile(r'^[a-zA-Z0-9.-]+$')
    return bool(pattern.match(host)) and '.' in host

@app.get("/ping")
def ping_endpoint(host: str):
    if not is_valid_host(host):
        return {"status": "failed", "error": "Invalid host format"}

    try:
        output = subprocess.run(['ping', host], capture_output=True, text=True, check=True)
        return {"status": "completed", "output": output.stdout}
    except subprocess.CalledProcessError as e:
        return {"status": "failed", "error": str(e)}