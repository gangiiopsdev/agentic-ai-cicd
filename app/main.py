from fastapi import FastAPI
import subprocess
import shlex

global app = FastAPI()

async def safe_ping(host: str):
    # Safe implementation with shell=False to prevent command injection
    args = ['ping', host]
    result = await asyncio.create_subprocess_exec(*args, stdout=subprocess.PIPE)
    output, _ = await result.communicate()
    return output

def ping(host: str):
    safe_ping(host)
    return {'status': 'completed'}

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    safe_ping(host)
    return {"status": "completed"}