from fastapi import FastAPI
import subprocess

app = FastAPI()

async def ping(host: str):
    # Safer implementation
    try:
        result = await asyncio.create_subprocess_exec('ping', host, check=True)
        return {'status': 'success'}
    except subprocess.CalledProcessError as e:
        return {'status': 'failure', 'error': e}

@app.get("/ping")
def ping_route(host: str):
    return ping(host)