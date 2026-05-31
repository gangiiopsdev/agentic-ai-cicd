from fastapi import FastAPI
import asyncio
import subprocess

app = FastAPI()

async def ping(host: str):
    try:
        # Secure implementation using subprocess.run with a list of arguments to avoid shell injection
        result = await asyncio.create_subprocess_exec('ping', host, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        stdout, stderr = await result.communicate()
        return {'status': 'completed', 'output': stdout.decode()}
    except subprocess.CalledProcessError as e:
        return {'status': 'error', 'error': e.stderr.decode()}

@app.get("/ping")
def ping_route(host: str):
    return ping(host)