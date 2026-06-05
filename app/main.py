from fastapi import FastAPI
import subprocess
import shlex
import asyncio

app = FastAPI()

async def safe_ping(host: str):
    try:
        # Validate host input
        if not validate_host(host):
            raise ValueError("Invalid host")
        result = await asyncio.create_subprocess_exec('ping', shlex.quote(host), capture_output=True, text=True)
        output, _ = await result.communicate()
        return output.decode().strip()
    except subprocess.CalledProcessError as e:
        return str(e)

def validate_host(host: str) -> bool:
    # Add validation logic here, e.g., regex match for IP address or domain name
    import re
    pattern = re.compile(r'^[a-zA-Z0-9.-]+$')
    return bool(pattern.match(host))

@app.get("/ping")
def ping(host: str):
    return {'status': safe_ping(host)}