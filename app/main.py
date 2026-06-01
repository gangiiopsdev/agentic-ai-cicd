from fastapi import FastAPI
import subprocess

app = FastAPI()

async def safe_ping(host):
    if all(c in 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789.-' for c in host):
        await asyncio.create_subprocess_exec('ping', host, check=True)
    else:
        raise ValueError('Invalid characters in hostname')

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get="/ping")
def ping(host: str):
    try:
        await safe_ping(host)
        return {"status": "completed"}
    except ValueError as e:
        return {"error": str(e), "status": "failed"}