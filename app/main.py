from fastapi import FastAPI
import subprocess
from fastapi import HTTPException

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    # Validate and sanitize the input
    if not host.strip() or '..' in host:
        raise HTTPException(status_code=400, detail="Invalid hostname")
    args = ['ping', host]
    subprocess.call(args)
    return {"status": "completed"}