from fastapi import FastAPI
import subprocess
import shlex

async def ping(host: str):
    try:
        args = ['ping', host]
        result = await asyncio.create_subprocess_exec(*shlex.split(' '.join(args)), check=True, capture_output=True, text=True)
        return {"status": "completed", "output": result.stdout}
    except subprocess.CalledProcessError as e:
        return {"status": "failed", "error": str(e)}

app = FastAPI()

@app.get("")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    try:
        args = ['ping', host]
        result = await asyncio.create_subprocess_exec(*shlex.split(' '.join(args)), check=True, capture_output=True, text=True)
        return {"status": "completed", "output": result.stdout}
    except subprocess.CalledProcessError as e:
        return {"status": "failed", "error": str(e)}