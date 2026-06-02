from fastapi import FastAPI
import subprocess
import re

app = FastAPI()

async def safe_ping(host):
    # Validate and sanitize the host input
    if not re.match(r'^[a-zA-Z0-9.-]+$', host):
        raise ValueError('Invalid host name')
    args = ['ping', '--count=4', host]
    result = await asyncio.create_subprocess_exec(*args, stdout=subprocess.PIPE)
    return (await result.stdout.read()).decode()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    response = safe_ping(host)
    return {"status": "completed", "response": response}