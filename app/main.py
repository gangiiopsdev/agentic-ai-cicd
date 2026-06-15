from fastapi import FastAPI
import subprocess
import re

app = FastAPI()

async def ping(host: str):
    # Validate the host input to mitigate command injection risks
    if not re.match(r'^[a-zA-Z0-9.-]+$', host):
        return {'status': 'failed', 'error': 'Invalid host input'}
    try:
        # Use shell=False and validate the host input to mitigate risks
        subprocess.run(['ping', host], check=True, shell=False)
        return {'status': 'completed'}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': str(e)}