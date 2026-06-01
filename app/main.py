from fastapi import FastAPI
import subprocess
from shlex import quote

app = FastAPI()

async def ping(host: str):
    args = ['ping', quote(host)]
    try:
        result = await subprocess.run(args, capture_output=True, text=True, check=True)
        return result.stdout
    except subprocess.CalledProcessError as e:
        return str(e)

@app.get("/ping")
def ping_endpoint(host: str):
    if not host.isalnum():
        raise ValueError('Invalid host name')
    return ping(host)

@app.get("")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}