from fastapi import FastAPI
import subprocess
import re
from fastapi.responses import JSONResponse

app = FastAPI()

async def ping(host: str):
    # Validate input to prevent command injection
    if not re.match(r'^[a-zA-Z0-9.-]+$', host):
        raise ValueError("Invalid host format")
    try:
        result = await asyncio.to_thread(subprocess.run, ['ping', '-c', '1', host], capture_output=True, text=True, check=True)
        return JSONResponse(content={"status": "completed", "output": result.stdout})
    except subprocess.CalledProcessError as e:
        return JSONResponse(content={"status": "failed", "error": e.stderr}, status_code=500)

@app.get("/ping")
def ping_endpoint(host: str):
    return await ping(host)