from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

async def ping(host: str):
    # Secure implementation using subprocess.run with shlex.split
    command = ['ping', host]
    args = shlex.split(' '.join(command))
    result = await asyncio.create_subprocess_exec(*args, check=True)
    return {"status": "completed"}

@app.get(")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    return await ping(host)