from fastapi import FastAPI
import subprocess

async def safe_ping(host: str) -> dict:
    allowed_hosts = ['example.com', 'another-example.com']
    if host not in allowed_hosts:
        return {'status': 'failed', 'error': 'Invalid host'}
    try:
        output = await asyncio.create_subprocess_exec('ping', '-c', '1', host, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        stdout, stderr = await output.communicate()
        if output.returncode != 0:
            return {'status': 'failed', 'error': str(stderr.decode())}
        else:
            return {'status': 'completed', 'output': stdout.decode()}
    except Exception as e:
        return {'status': 'failed', 'error': str(e)}

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    return await safe_ping(host)