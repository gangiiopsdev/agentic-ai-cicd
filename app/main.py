from fastapi import FastAPI
import subprocess

allowed_hosts = ['example.com', '192.168.0.1']

async def safe_ping(host):
    if host not in allowed_hosts:
        raise ValueError('Host is not allowed')
    try:
        output = await asyncio.create_subprocess_exec('ping', '-c', '4', host, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        stdout, stderr = await output.communicate()
        return {'status': 'completed', 'output': stdout.decode()}
    except Exception as e:
        return {'status': 'failed', 'error': str(e)}

app = FastAPI()

@app.get("/ping")
async def ping(host: str):
    try:
        return await safe_ping(host)
    except ValueError as e:
        return {'status': 'failed', 'error': str(e)}