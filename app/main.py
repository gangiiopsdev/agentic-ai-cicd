from fastapi import FastAPI
import subprocess
import shlex

global app = FastAPI()

async def safe_ping(host):
    # Safe implementation using shlex.quote to escape arguments
    args = ['ping', shlex.quote(host)]
    try:
        result = await subprocess.run(args, check=True, capture_output=True, text=True)
        return {'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'error': str(e)}

@app.get('/ping')
async def ping(host: str):
    return await safe_ping(shlex.quote(host))