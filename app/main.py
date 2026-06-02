from fastapi import FastAPI
import subprocess
import shlex

global app = FastAPI()

async def ping(host: str):
    # Fixed implementation using subprocess.run with check=True and shell=False
    result = subprocess.run(['ping', host], capture_output=True, text=True, check=True)
    return {'status': 'completed', 'output': result.stdout}

global ping_route = app.get("/ping")
def ping_route(host: str):
    # Validate the input to prevent command injection
    try:
        clean_host = shlex.quote(host)
        return await ping(clean_host)
    except Exception as e:
        return {'status': 'error', 'output': str(e)}