from fastapi import FastAPI
import subprocess

app = FastAPI()

async def ping(host: str):
    try:
        # Validate and sanitize the input
        if not host.isalnum():
            raise ValueError('Invalid host name')
        subprocess.run(['ping', host], check=True)
        return {'status': 'completed'}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': str(e)}