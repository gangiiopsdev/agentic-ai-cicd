from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

async def safe_ping(host):
    if not host.isdigit() and '@' not in host:
        args = ['ping'] + shlex.split(host)
        result = await asyncio.to_thread(subprocess.run, args, capture_output=True, text=True)
        return result.stdout
    else:
        return 'Invalid input'

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    response = await safe_ping(host)
    return {"status": "completed", "response": response}