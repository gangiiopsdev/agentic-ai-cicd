from fastapi import FastAPI
import subprocess
import shlex

def validate_host(host: str) -> bool:
    try:
        int(host)
        return True
    except ValueError:
        return False

async def ping(host: str):
    if not validate_host(host):
        raise ValueError('Invalid input')
    try:
        result = await asyncio.create_subprocess_exec('ping', *shlex.split(host), stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        output, _ = await result.communicate()
        return {'status': 'completed', 'output': output.decode().strip()}
    except Exception as e:
        return {'status': 'error', 'message': str(e)}

app = FastAPI()
@app.get("/ping")
def ping_endpoint(host: str):
    if not validate_host(host) or host.startswith('-'):
        raise ValueError('Invalid input')
    return await ping(host)