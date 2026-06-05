from fastapi import FastAPI
import subprocess

app = FastAPI()

async def safe_ping(host):
    args = ['ping', host]
    result = await asyncio.create_subprocess_exec(*args, capture_output=True, text=True)
    return result.stdout

@app.get("/ping")
def ping(host: str):
    return {"status": "completed", "output": safe_ping(host)}