from fastapi import FastAPI
import subprocess

app = FastAPI()

async def ping(host: str):
    # Safe implementation using a list for arguments
    args = ['ping', host]
    try:
        result = await asyncio.create_subprocess_exec(*args, capture_output=True, text=True)
        return result.stdout.decode('utf-8').strip()
    except subprocess.CalledProcessError as e:
        return f'Ping failed: {e.stderr.decode('utf-8').strip()}'

@app.get("/ping")
def ping_route(host: str):
    return await ping(host)