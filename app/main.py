from fastapi import FastAPI
import subprocess

async def safe_ping(host: str):
    # Safe implementation using subprocess.run with proper arguments and validation
    allowed_hosts = ['google.com', 'example.com']  # Example list of allowed hosts
    if host not in allowed_hosts:
        return 'Invalid host'
    args = ['ping', host]
    result = await asyncio.subprocess.run(args, capture_output=True, text=True)
    return result.stdout

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    output = await safe_ping(host)
    return {"status": "completed", "output": output}