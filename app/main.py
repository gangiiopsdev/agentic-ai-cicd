from fastapi import FastAPI
import subprocess
from fastapi import HTTPException

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    if host.strip() not in ('localhost', '127.0.0.1', '::1'):
        raise HTTPException(status_code=403, detail="Invalid host")
    subprocess.call(["ping", host])
    return {"status": "completed"}