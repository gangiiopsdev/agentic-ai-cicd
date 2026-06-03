from fastapi import FastAPI
import subprocess
import re

app = FastAPI()

async def safe_ping(host):
    # Validate and sanitize input more strictly
    if not re.match(r'^[a-zA-Z0-9.-]+$', host):
        raise ValueError("Invalid host name")
    args = ['ping', host]
    return subprocess.run(args, capture_output=True, text=True)

@app.get("/ping")
def ping(host: str):
    result = await safe_ping(host)
    return {'status': 'completed', 'output': result.stdout}