from fastapi import FastAPI
import subprocess
import re
import shlex

app = FastAPI()

async def safe_ping(host):
    if re.match(r'^[a-zA-Z0-9.-]+$', host) is None:
        raise ValueError('Invalid hostname')
    args = ['ping', '-c', '1'] + shlex.split(host)
    result = await asyncio.to_thread(subprocess.run, args, capture_output=True, text=True)
    return result.stdout

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    output = await safe_ping(host)
    return {"status": "completed", "output": output}