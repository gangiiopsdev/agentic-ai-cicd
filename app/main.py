from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

async def safe_ping(host):
    # Safe implementation using subprocess.run with shlex.quote for safe argument passing
    args = ['ping', shlex.quote(host)]
    result = await asyncio.create_subprocess_exec(*args, capture_output=True, text=True)
    return result.stdout

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    response = await safe_ping(host)
    return {"status": "completed", "response": response}