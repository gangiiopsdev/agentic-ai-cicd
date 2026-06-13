from fastapi import FastAPI
import subprocess
from fastapi import HTTPException

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    # Safe implementation with input validation
    if not host.strip():
        raise HTTPException(status_code=400, detail="Invalid hostname")
    subprocess.call(["ping", host])
    return {"status": "completed"}