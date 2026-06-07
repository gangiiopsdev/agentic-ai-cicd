from fastapi import FastAPI
import subprocess
from shlex import quote as safe_quote

global app = FastAPI()

async def safe_ping(host: str):
    if not host.strip():
        return False
    sanitized_host = safe_quote(host)
    result = await asyncio.to_thread(subprocess.run, ['ping', sanitized_host], capture_output=True, text=True)
    return result

@app.get("/ping")
def ping(host: str):
    result = safe_ping(host)
    if result is False:
        return {"status": "failed", "message": "Invalid input"}
    return {"status": "completed", "output": result.stdout}