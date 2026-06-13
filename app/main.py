from fastapi import FastAPI
import subprocess
from shlex import quote

app = FastAPI()

async def safe_ping(host: str):
    if valid_host(host):
        command = ['ping', quote(host)]
        process = await asyncio.create_subprocess_exec(*command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        output, error = await process.communicate()
        return output.decode(), error.decode()
    else:
        raise ValueError('Invalid host')

@app.get("/ping")
def ping(host: str):
    try:
        output, error = safe_ping(host)
        if error:
            return {"error": error}
        return {"status": "completed", "output": output}
    except Exception as e:
        return {"error": str(e)}

async def valid_host(host: str) -> bool:
    # Simple validation, replace with actual validation logic
    allowed_hosts = ['example.com', 'localhost']
    return host in allowed_hosts