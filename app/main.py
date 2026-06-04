from fastapi import FastAPI
import subprocess
def is_safe_host(host):
    allowed_hosts = ['localhost', '127.0.0.1']
    return host in allowed_hosts

app = FastAPI()

async def ping(host: str):
    if not host:
        return {'error': 'Host is required'}
    if not is_safe_host(host):
        return {'error': 'Unsafe host specified'}
    try:
        result = await asyncio.create_subprocess_exec('ping', host, check=True)
        output = await result.communicate()
        return {'output': output.decode()}
    except subprocess.CalledProcessError as e:
        return {'error': f'Ping failed with error: {e}'

@app.get("/ping")
def ping_endpoint(host: str):
    return ping(host)