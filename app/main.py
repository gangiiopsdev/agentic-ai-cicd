from fastapi import FastAPI
import subprocess
from typing import Union

app = FastAPI()

def is_valid_host(host: str) -> bool:
    return host.isalnum() and len(host) <= 20

@app.get("/ping")
def ping(host: str) -> Union[dict, dict]:
    if not is_valid_host(host):
        return {"error": "Invalid host"}

    # Secure implementation using subprocess.run with shell=False and check=True
    try:
        result = subprocess.run(["ping", host], capture_output=True, text=True, check=True)
        return {"status": "completed", "output": result.stdout}
    except subprocess.CalledProcessError as e:
        return {"error": str(e)}