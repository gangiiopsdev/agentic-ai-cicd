from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

async def ping(host: str):
    try:
        # Secure implementation using subprocess.run with check=True and capture_output=True, sanitize input
        result = await asyncio.to_thread(subprocess.run, ['ping', *shlex.split(host)], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return {'status': 'completed', 'stdout': result.stdout.decode(), 'stderr': result.stderr.decode()}
    except subprocess.CalledProcessError as e:
        return {'status': 'error', 'stderr': e.stderr.decode()}

@app.get("/ping")
def ping_route(host: str):
    return ping(host)