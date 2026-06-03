from fastapi import FastAPI, HTTPException
import subprocess
import shlex

global app = FastAPI()

async def ping(host: str):
    # Use os.path.abspath to ensure the executable path is full and shlex.split to handle command arguments safely
    command = ['ping', '-c', '1'] + shlex.split(host)
    result = subprocess.run(command, capture_output=True, text=True, check=True)
    return {'host': host, 'result': result.stdout}

def ping_endpoint(request):
    return await ping(request.query_params.get('host'))