from fastapi import FastAPI
import subprocess
allowed_hosts = ['example.com', 'localhost']

async def safe_ping(host: str):
    if host not in allowed_hosts:
        raise ValueError('Invalid host')
    try:
        result = await asyncio.create_subprocess_exec('ping', host, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        stdout, stderr = await result.communicate()
        return {'status': 'completed', 'output': stdout.decode()}
    except Exception as e:
        return {'status': 'failed', 'error': str(e)}

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    return await safe_ping(host)