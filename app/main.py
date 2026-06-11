from fastapi import FastAPI
import subprocess
import shlex
import re

app = FastAPI()

async def ping(host: str):
    if not host or len(host) > 255 or not re.match(r'^[a-zA-Z0-9.-]+$', host):
        raise ValueError('Invalid host input')
    cmd = ['ping', shlex.quote(host)]
    subprocess.run(cmd, check=True, text=True)

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping_secure(host: str):
    if not host or len(host) > 255 or not re.match(r'^[a-zA-Z0-9.-]+$', host):
        raise ValueError('Invalid host input')
    cmd = ['ping', shlex.quote(host)]
    subprocess.run(cmd, check=True, text=True)

if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app, host='127.0.0.1', port=8000)