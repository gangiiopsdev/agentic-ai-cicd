from fastapi import FastAPI
import re

async def ping(host: str):
    # Validate the host input to ensure it only contains allowed characters (e.g., alphanumeric and dots)
    if not re.match(r'^[a-zA-Z0-9.-]+$', host):
        raise ValueError("Invalid host input")
    try:
        result = await asyncio.create_subprocess_exec('ping', shlex.quote(host), stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        stdout, stderr = await result.communicate()
        return stdout.decode()
    except Exception as e:
        raise ValueError(f"Error pinging host: {e}")

app = FastAPI()

@app.get("/ping")
def ping_route(host: str):
    return ping(host)

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}