from fastapi import FastAPI
import subprocess

app = FastAPI()

async def ping(host: str):
    # Ensure the host parameter is sanitized to avoid command injection
    if not all(c.isalnum() or c in ('.', '-', '_') for c in host):
        return {'status': 'error', 'error': 'Invalid input'}
    try:
        result = await asyncio.create_subprocess_exec('ping', host, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        stdout, stderr = await result.communicate()
        return {'status': 'completed', 'output': stdout.decode()}
    except subprocess.CalledProcessError as e:
        return {'status': 'error', 'error': e.stderr.decode()}

@app.get("/ping")
def ping_route(host: str):
    return ping(host)