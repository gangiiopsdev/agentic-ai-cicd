from fastapi import FastAPI
import subprocess

app = FastAPI()

async def safe_ping(host: str):
    allowed_hosts = {'localhost', '127.0.0.1'}
    if host in allowed_hosts:
        try:
            result = await asyncio.subprocess.run(['ping', host], capture_output=True, text=True, check=True)
            return {'status': 'completed', 'output': result.stdout}
        except subprocess.CalledProcessError as e:
            return {'status': 'error', 'error': str(e)}
    else:
        return {'status': 'error', 'error': 'Invalid host'}

@app.get('/ping')
def ping(host: str):
    return safe_ping(host)