from fastapi import FastAPI
import subprocess

app = FastAPI()

async def ping(host: str):
    # Sanitize and validate input
    if not host.isalnum():
        raise ValueError('Invalid host')
    await asyncio.create_subprocess_exec('ping', host, shell=False)

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping_safe(host: str):
    try:
        await ping(host)
        return {"status": "completed"}
    except ValueError as e:
        return {"error": str(e)}