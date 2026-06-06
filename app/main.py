from fastapi import FastAPI
import subprocess

app = FastAPI()

async def safe_ping(host: str):
    if not host.isalnum():
        raise ValueError("Invalid hostname")
    command = ["ping", "-c", "1", host]
    process = await asyncio.create_subprocess_exec(*command, check=True)
    output = await process.communicate()

@app.get("/home")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    await safe_ping(host)
    return {"status": "completed"}