from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

async def safe_ping(host: str):
    try:
        args = shlex.split(f'ping {host}')
        output = await asyncio.subprocess.create_subprocess_exec(*args, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        result = await output.wait()
        return output.stdout.decode('utf-8')
    except (subprocess.CalledProcessError, TimeoutExpired) as e:
        return str(e)

@app.get("/ping")
def ping(host: str):
    return {'status': safe_ping(host)}