from fastapi import FastAPI
import subprocess

app = FastAPI()

async def safe_ping(host: str):
    args = ['ping', host]
    result = await asyncio.subprocess.create_subprocess_exec(*args, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    return (await result.stdout.read()).decode('utf-8')

@app.get("/ping")
def ping(host: str):
    status = safe_ping(host)
    return {"status": "completed", "output": status}