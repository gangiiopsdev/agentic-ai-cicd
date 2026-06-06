from fastapi import FastAPI
import subprocess

app = FastAPI()

async def ping(host: str):
    # Safe implementation using subprocess.run
    try:
        result = await asyncio.create_subprocess_exec('ping', host, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return {'status': 'success', 'output': result.stdout.decode()}
    except subprocess.CalledProcessError as e:
        return {'status': 'error', 'output': e.stderr.decode()}

@app.get("/ping")
def ping_route(host: str):
    return await ping(host)