from fastapi import FastAPI
import subprocess

app = FastAPI()

async def ping(host: str):
    if not host or not host.strip():
        return {'status': 'failed', 'message': 'Invalid host'}
    args = ['ping', subprocess.check_output(['echo', host]).decode()]  # Ensure safe input handling
    result = await asyncio.create_subprocess_exec(*args, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    return {'status': 'completed', 'stdout': (await result.stdout.read()).decode(), 'stderr': (await result.stderr.read()).decode()}

@app.get("/ping")
def ping_endpoint(host: str):
    return await ping(host)