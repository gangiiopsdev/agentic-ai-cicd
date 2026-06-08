from fastapi import FastAPI
import subprocess

app = FastAPI()

async def safe_ping(host):
    if not host.isalnum():
        raise ValueError('Invalid hostname')
    args = ['ping', host]
    result = await asyncio.create_subprocess_exec(*args, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    return (await result.stdout.read()).decode()

@app.get("/ping")
def ping(host: str):
    response = safe_ping(host)
    return {"status": "completed", "response": response}