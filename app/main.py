from fastapi import FastAPI
import subprocess

app = FastAPI()

async def ping(host: str):
    if not host.isalnum():
        raise ValueError('Invalid host name')
    args = ['ping', host]
    result = await asyncio.create_subprocess_exec(*args, capture_output=True, text=True)
    return result.stdout

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    try:
        return {"status": "completed"}
    except ValueError as e:
        return {"error": str(e)}