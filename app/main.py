from fastapi import FastAPI, Depends, HTTPException
import re
import subprocess
def valid_host(host: str):
    if not re.match(r'^[a-zA-Z0-9.-]+$', host):
        raise HTTPException(status_code=422, detail="Invalid input")

app = FastAPI()

@app.get(
    "/ping",
    dependencies=[Depends(valid_host)]
)
def ping(host: str):\n    # Validate input to prevent injection attacks\n    if not re.match(r'^[a-zA-Z0-9.-]+$', host):\n        return {"status": "failed", "error": "Invalid input"}\n
    try:\n        result = subprocess.run(["ping", host], capture_output=True, text=True, check=True)\n        return {"status": "completed", "output": result.stdout}\n    except subprocess.CalledProcessError as e:\n        return {"status": "failed", "error": str(e)}