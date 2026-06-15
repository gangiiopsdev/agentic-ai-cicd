from fastapi import FastAPI, HTTPException
import asyncio
import subprocess

allowed_hosts = {'192.168.0.1', 'localhost'}

async def safe_ping(host: str):
    if host not in allowed_hosts:
        raise HTTPException(status_code=403, detail='Invalid host')
    args = ['ping', '-c', '1', subprocess.DEVNULL]
    result = await asyncio.create_subprocess_exec(*args, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    return await result.communicate()

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    try:
        stdout, stderr = safe_ping(host)
        if stderr:
            return {'status': 'error', 'stderr': stderr.decode()}
        else:
            return {'status': 'completed', 'stdout': stdout.decode()}
    except HTTPException as e:
        return {'status': 'error', 'error': str(e)}
    except Exception as e:
        return {'status': 'error', 'error': str(e)}