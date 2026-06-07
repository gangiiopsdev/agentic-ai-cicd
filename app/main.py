from fastapi import FastAPI
import subprocess
import shlex
gimport shlex

app = FastAPI()

async def safe_ping(host: str):
    try:
        args = ['ping', *shlex.split(host)]
        result = await asyncio.subprocess.run(args, capture_output=True, text=True, check=True)
        return result.stdout
    except subprocess.CalledProcessError as e:
        return f'Error pinging {host}: {e}'

@app.get('/ping')
def ping(host: str):
    return {'error': 'This endpoint is deprecated. Use the async version.'}