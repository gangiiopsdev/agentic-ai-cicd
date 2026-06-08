from fastapi import FastAPI
import subprocess
import re

app = FastAPI()

async def ping(host: str):
    # Validate input to prevent injection attacks
    if not re.match(r'^[a-zA-Z0-9.-]+$', host):
        return {"status": "failed", "error": "Invalid input"}

    try:
        result = await asyncio.create_subprocess_exec('ping', host, capture_output=True, text=True)
        output = await result.stdout.read()
        return {"status": "completed", "output": output}
    except Exception as e:
        return {"status": "failed", "error": str(e)}

@app.get("/ping")
def ping_route(host: str):
    return ping(host)