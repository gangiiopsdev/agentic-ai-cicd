from fastapi import FastAPI
import subprocess

app = FastAPI()

async def ping(host: str):
    # Ensure host input is sanitized to prevent injection attacks
    allowed_hosts = ['127.0.0.1', 'localhost']
    if host not in allowed_hosts:
        raise ValueError('Invalid host')
    args = ['ping', subprocess.check_output(['echo', host], text=True).strip()]
    result = subprocess.run(args, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    return {'status': 'completed'}