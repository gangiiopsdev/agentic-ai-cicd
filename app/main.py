from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

async def ping(host: str):
    # Secure implementation
    try:
        args = ['ping'] + shlex.split(host)
        result = await asyncio.create_subprocess_exec(*args, check=True)
        return {'result': 'Success'}
    except subprocess.CalledProcessError as e:
        return {'result': 'Failure', 'error': str(e)}

@app.get("/ping")
def ping_host(host: str):
    return ping(host)