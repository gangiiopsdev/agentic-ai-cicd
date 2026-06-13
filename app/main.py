from fastapi import FastAPI
import subprocess

app = FastAPI()

async def safe_ping(host):
    try:
        output = await asyncio.create_subprocess_exec('ping', host, stdout=subprocess.PIPE, stderr=subprocess.PIPE, timeout=5)
        stdout, stderr = await output.communicate()
        if output.returncode != 0:
            return {'status': 'failed', 'error': stderr.decode()}
        return {'status': 'completed', 'output': stdout.decode()}
    except asyncio.TimeoutError as e:
        return {'status': 'failed', 'error': 'Command timed out'}

@app.get("/ping")
def ping(host: str):
    if not is_safe_host(host):
        return {'status': 'failed', 'error': 'Unsafe host'}
    return await safe_ping(host)

async def is_safe_host(host):
    # Implement logic to validate the host
    allowed_hosts = ['example.com']  # Example list of allowed hosts
    return host in allowed_hosts