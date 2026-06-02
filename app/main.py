from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

async def ping_safe(host: str):
    # Safe implementation using list to avoid shell=True and validate input
    if not host.isalnum():
        raise ValueError('Invalid hostname')
    args = shlex.split('ping ' + host)
    subprocess.call(args)

@app.get("/ping")
def ping(host: str):
    await ping_safe(host)
    return {"status": "completed"}