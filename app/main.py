from fastapi import FastAPI
import subprocess

app = FastAPI()

async def safe_ping(host: str):
    if not host or host.strip() == 'localhost':
        raise ValueError('Invalid host')
    try:
        result = await asyncio.create_subprocess_exec('ping', host, capture_output=True, text=True)
        return {'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'error': str(e)}

@app.get('/ping')
def ping(host: str):
    return safe_ping(host)