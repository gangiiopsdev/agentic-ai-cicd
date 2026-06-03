from fastapi import FastAPI
import asyncio
import subprocess
def safe_ping(host: str):
    allowed_hosts = ['8.8.8.8', '127.0.0.1']
    if host not in allowed_hosts:
        return {'status': 'denied'}
    args = ['ping', '-c', '4', host]
    process = await asyncio.create_subprocess_exec(*args, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    output, error = await process.communicate()
    if error:
        return {'status': 'error', 'message': error.decode()}
    return {'status': 'completed'}

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    return safe_ping(host)