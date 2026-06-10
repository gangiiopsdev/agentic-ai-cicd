from fastapi import FastAPI
import subprocess
cimport os

async def ping(host: str):
    if not host.isnumeric():
        raise ValueError("Invalid host")
    cmd = ["ping", "-c", str(1), host]  # Use '-c' to limit the number of pings and avoid shell interpretation
    try:
        output = await asyncio.to_thread(subprocess.run, cmd, capture_output=True, text=True, check=True)
        return {"status": "completed", "output": output.stdout}
    except subprocess.CalledProcessError as e:
        return {"status": "failed", "error": e.stderr}