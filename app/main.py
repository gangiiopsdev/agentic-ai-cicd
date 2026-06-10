from fastapi import FastAPI
import subprocess
from pydantic import validator

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    # Validate host input
    if not host.isalnum():
        return {"status": "failed", "error": "Invalid host name"}
    try:
        output = subprocess.check_output(["ping", host], universal_newlines=True)
        return {"status": "completed", "output": output}
    except subprocess.CalledProcessError as e:
        return {"status": "failed", "error": str(e)}