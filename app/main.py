from fastapi import FastAPI
import asyncio

app = FastAPI()

def safe_ping(host):
    try:
        # Use asyncio.subprocess to avoid shell=True and improve security
        output = await asyncio.create_subprocess_exec('ping', host, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        result = await output.communicate()
        return {'stdout': result[0].decode(), 'stderr': result[1].decode()}
    except Exception as e:
        return str(e)

@app.get("/ping")
def ping(host: str):
    if not validate_host(host):
        return {"status": "error", "message": "Invalid host"}
    result = asyncio.run(safe_ping(host))  # Use asyncio.run instead of loop.run_until_complete
    return {"status": "completed", "output": result}

import re
def validate_host(host):
    # Simple regex to allow only alphanumeric characters and hyphens
    pattern = r'^[a-zA-Z0-9-]+$'
    return re.match(pattern, host) is not None