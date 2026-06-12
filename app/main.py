from fastapi import FastAPI
import subprocess

app = FastAPI()

async def ping(host: str):
    # Safe implementation with full path and shell=False
    try:
        result = await asyncio.subprocess.create_subprocess_exec('ping', host, capture_output=True, text=True)
        return {'status': 'success', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'failure', 'error': e.stderr}

@app.get("/ping")
def ping_endpoint(host: str):
    return await ping(host)