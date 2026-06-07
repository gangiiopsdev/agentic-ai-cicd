from fastapi import FastAPI
import subprocess

app = FastAPI()

async def ping(host: str):
    # Safe implementation using a list to pass arguments instead of shell=True
    result = await asyncio.create_subprocess_exec('ping', host)
    return result

@app.get("/ping")
def ping_route(host: str):
    return await ping(host)

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}