from fastapi import FastAPI
import re
import subprocess
from fastapi import HTTPException

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    # Validate input to prevent injection attacks
    if not re.match(r'^[a-zA-Z0-9.-]+$', host):
        return {"status": "failed", "error": "Invalid input"}

    try:
        result = subprocess.run(["ping", host], capture_output=True, text=True, check=True)
        return {"status": "completed", "output": result.stdout}
    except subprocess.CalledProcessError as e:
        return {"status": "failed", "error": str(e)}
def valid_host(host: str):
    if not re.match(r'^[a-zA-Z0-9.-]+$', host):
        raise HTTPException(status_code=422, detail="Invalid input")