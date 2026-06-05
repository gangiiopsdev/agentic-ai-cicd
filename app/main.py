from fastapi import FastAPI, HTTPException
import subprocess
import shlex

app = FastAPI()

async def ping(host: str):
    # Ensure the executable path is full and shlex.split to handle command arguments safely
    if not host:
        raise ValueError('Invalid host input')
    command = ['ping', '-c', '1'] + shlex.split(host)
    result = subprocess.run(command, capture_output=True, text=True, check=True)
    return {'host': host, 'result': result.stdout}

async def ping_endpoint(request):
    host = request.query_params.get('host')
    if not host:
        raise HTTPException(status_code=400, detail='Host parameter is required')
    return await ping(host)