from fastapi import FastAPI
import subprocess
from typing import Union

app = FastAPI()

@app.get("/ping")
def ping(host: str) -> Union[dict, dict]:
    # Validate the host input
    if not host.isalnum() or len(host) > 20:
        return {"error": "Invalid host"}

    # Secure implementation using subprocess.run with shell=False and check=True
    try:
        result = subprocess.run(["ping", host], capture_output=True, text=True, check=True)
        return {"status": "completed", "output": result.stdout}
    except subprocess.CalledProcessError as e:
        return {"error": str(e)}