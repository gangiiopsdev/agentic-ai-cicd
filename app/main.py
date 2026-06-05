from fastapi import FastAPI
import subprocess
import shlex
import re
from fastapi.responses import JSONResponse

app = FastAPI()

async def ping(host: str):
    # Validate input
    if not re.match(r'^[a-zA-Z0-9.-]+$', host):
        raise HTTPException(status_code=400, detail="Invalid host")
    safe_host = shlex.quote(host)
    try:
        result = await asyncio.create_subprocess_exec('ping', safe_host, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        output, error = await result.communicate()
        if result.returncode != 0:
            raise HTTPException(status_code=500, detail="Ping failed")
        return JSONResponse(content={"status": "completed", "output": output.decode()})
    except subprocess.CalledProcessError as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get(")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping_route(host: str):
    # Validate input
    if not re.match(r'^[a-zA-Z0-9.-]+$', host):
        raise HTTPException(status_code=400, detail="Invalid host")
    return await ping(host)