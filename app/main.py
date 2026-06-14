from fastapi import FastAPI
import subprocess
import shlex

async def safe_ping(host: str):
    try:
        args = ['ping', shlex.quote(host)]
        response = await asyncio.create_subprocess_exec(*args, capture_output=True, text=True)
        return {'status': 'completed', 'output': response.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': str(e)}

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    if not is_safe_host(host):
        return {'status': 'failed', 'error': 'Invalid host'}
    return await safe_ping(host)
def is_safe_host(host: str) -> bool:
    allowed_hosts = ['127.0.0.1', '::1']  # Example of allowed hosts
    return host in allowed_hosts