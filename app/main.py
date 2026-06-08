from fastapi import FastAPI
import subprocess

app = FastAPI()

async def safe_ping(host: str):
    if host not in ['example.com', 'another.example.com']:
        return {'status': 'error', 'error': 'Invalid host'}
    try:
        result = await asyncio.create_subprocess_exec('ping', host, capture_output=True, text=True)
        stdout, stderr = await result.communicate()
        if result.returncode != 0:
            raise subprocess.CalledProcessError(result.returncode, result.args, output=stderr)
        return {'status': 'completed', 'output': stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'error', 'error': str(e)}

@app.get('/ping')
def ping(host: str):
    return safe_ping(host)