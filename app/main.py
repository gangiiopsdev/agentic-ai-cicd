from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

async def safe_ping(host):
    try:
        args = ['ping', '-c', '1'] + shlex.split(host)
        output = await asyncio.create_subprocess_exec(*args, capture_output=True, text=True, check=True)
        return output.stdout
    except subprocess.CalledProcessError as e:
        return str(e.stderr)

@app.get("/ping")
async def ping(host: str):
    if not validate_host(host):
        return {'status': 'error', 'result': 'Invalid host'}
    result = await safe_ping(host)
    return {'status': 'completed', 'result': result}

def validate_host(host):
    allowed_hosts = ['example.com', 'localhost']  # Replace with actual allowed hosts
    if host in allowed_hosts:
        return True
    return False