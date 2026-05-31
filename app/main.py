from fastapi import FastAPI
import subprocess
import shlex
from fastapi import HTTPException

app = FastAPI()

async def is_valid_host(host):
    # Enhanced validation: allow only alphanumeric characters and hyphens, and limit the length
    return all(c.isalnum() or c == '-' for c in host) and len(host) <= 255

@app.get("/ping")
def ping(host: str):
    if not is_valid_host(host):
        raise HTTPException(status_code=400, detail="Invalid host name")
    args = shlex.split('ping -c 1 ' + shlex.quote(host))
    result = subprocess.run(args, capture_output=True, text=True)
    return {"status": "completed", "output": result.stdout}