from fastapi import FastAPI, HTTPException
import asyncio
from subprocess import Popen, PIPE

allowed_hosts = {'192.168.0.1', 'localhost'}

async def safe_ping(host: str):
    if host not in allowed_hosts:
        raise HTTPException(status_code=403, detail='Invalid host')
    process = Popen(['ping', '-c', '1', host], stdout=PIPE, stderr=PIPE)
    stdout, stderr = await asyncio.to_thread(process.communicate)
    return stdout, stderr

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    try:
        stdout, stderr = await safe_ping(host)
        if stderr:
            return {'status': 'error', 'stderr': stderr.decode()}
        else:
            return {'status': 'completed', 'stdout': stdout.decode()}
    except HTTPException as e:
        return {'status': 'error', 'error': str(e)}
    except Exception as e:
        return {'status': 'error', 'error': str(e)}