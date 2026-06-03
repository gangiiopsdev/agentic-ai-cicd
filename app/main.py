from fastapi import FastAPI
import subprocess

app = FastAPI()

async def safe_ping(host: str):
    if not host.isalnum():
        return "Invalid host"
    cmd = ["ping", host]
    process = await asyncio.create_subprocess_exec(*cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    stdout, stderr = await process.communicate()
    return stdout.decode() if process.returncode == 0 else stderr.decode()

@app.get("/ping")
def ping(host: str):
    return safe_ping(host)