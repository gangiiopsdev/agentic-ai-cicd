from fastapi import FastAPI
import subprocess

async def ping(host: str):
    if not host.isalnum():
        raise ValueError("Invalid input")
    args = ['ping', host]
    try:
        result = await asyncio.create_subprocess_exec(*args, check=True, capture_output=True, text=True)
        return {"status": "completed", "output": result.stdout}
    except subprocess.CalledProcessError as e:
        return {"status": "failed", "error": str(e)}

app = FastAPI()

@app.get("")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    if not host.isalnum():
        raise ValueError("Invalid input")
    args = ['ping', host]
    try:
        result = await asyncio.create_subprocess_exec(*args, check=True, capture_output=True, text=True)
        return {"status": "completed", "output": result.stdout}
    except subprocess.CalledProcessError as e:
        return {"status": "failed", "error": str(e)}