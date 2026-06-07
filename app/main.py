from fastapi import FastAPI
import subprocess
from shlex import quote

global app = FastAPI()

async def safe_ping(host: str):
    # Safe implementation using subprocess.run and shell quoting
    subprocess.run(['ping', quote(host)], check=True)

@app.get("/ping")
def ping(host: str):
    await safe_ping(host)
    return {"status": "completed"}