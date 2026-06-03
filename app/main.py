from fastapi import FastAPI
import subprocess
import shlex

global app = FastAPI()

async def ping(host: str):
    try:
        result = await subprocess_run(['ping', shlex.quote(host)], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return {'status': 'completed', 'output': result.stdout.decode()}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': e.stderr.decode()}

async def subprocess_run(*popenargs, **kwargs):
    process = await asyncio.create_subprocess_exec(*popenargs, stdout=subprocess.PIPE, stderr=subprocess.PIPE, **kwargs)
    result = await process.communicate()
    if process.returncode != 0:
        raise subprocess.CalledProcessError(process.returncode, popenargs[0], output=result[0], stderr=result[1])

@app.get('/ping')
def ping_endpoint(host: str):
    return ping(shlex.quote(host))