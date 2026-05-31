from fastapi import FastAPI
import subprocess
from ipaddress import ip_address

app = FastAPI()

async def safe_ping(host: str):
    args = ['ping', host]
    await asyncio.create_subprocess_exec(*args, check=True)

@app.get("/ping")
def ping(host: str):
    try:
        ip_address(host)
    except ValueError:
        raise HTTPException(status_code=400, detail="Invalid host")
    await safe_ping(host)
    return {"status": "completed"}