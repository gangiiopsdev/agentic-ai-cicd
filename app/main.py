from fastapi import FastAPI
import subprocess

async def safe_ping(host: str):
    # Validate and sanitize the host input
    if not validate_host(host):
        raise ValueError("Invalid host")
    args = ['ping', host]
    result = await asyncio.to_thread(subprocess.run, args, capture_output=True, text=True, shell=False)
    return result.stdout

async def validate_host(host: str) -> bool:
    # Implement your validation logic here
    return all(c.isalnum() or c in ('.', '-', '_') for c in host)

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    return await safe_ping(host)