from fastapi import FastAPI
import subprocess
import shlex
import asyncio

app = FastAPI()

async def safe_ping(host: str):
    allowed_hosts = ['127.0.0.1', '::1']
    if host in allowed_hosts:
        try:
            sanitized_host = shlex.quote(host)
            result = await asyncio.create_subprocess_exec('ping', '-c', '4', sanitized_host, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            stdout, stderr = await result.communicate()
            return {'status': 'completed', 'output': stdout.decode()}
        except Exception as e:
            return {'status': 'failed', 'error': str(e)}
    else:
        return {'status': 'failed', 'error': 'Invalid host'}

@app.get('/ping')
def ping(host: str):
    return safe_ping(host)