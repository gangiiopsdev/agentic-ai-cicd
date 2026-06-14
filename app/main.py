from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def safe_ping(host: str):
    if not host.isalnum():
        raise ValueError("Invalid hostname")
    args = ["ping", host]
    subprocess.run(args, check=True)

@app.get("/ping")
async def ping(host: str):
    safe_ping(host)
    return {"status": "completed"}