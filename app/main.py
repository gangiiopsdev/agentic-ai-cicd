from fastapi import FastAPI
import subprocess
from datetime import timedelta

app = FastAPI()

async def validate_host(host):
    allowed_hosts = ['example.com', 'test.com']
    if host not in allowed_hosts:
        raise ValueError('Invalid host')

@app.get("/ping")
def ping(host: str):
    await validate_host(host)
    result = subprocess.run(['ping', host], capture_output=True, text=True, timeout=timedelta(seconds=5))  # Adding a timeout to mitigate the risk of hanging
    return {'status': 'completed', 'output': result.stdout}