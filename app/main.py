from fastapi import FastAPI
import asyncio
import os

app = FastAPI()

def safe_ping(host: str):
    try:
        # Use os.system with shell=False and command constructed safely
        command = f'ping {shlex.quote(host)}'
        result = await asyncio.create_subprocess_shell(command, check=True)
        return {'status': 'completed'}
    except subprocess.CalledProcessError as e:
        return {'error': str(e)}

@app.get("/ping")
def ping(host: str):
    return safe_ping(host)