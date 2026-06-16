from fastapi import FastAPI
import subprocess

app = FastAPI()

async def safe_ping(host):
    try:
        result = await asyncio.create_subprocess_exec('ping', host, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, timeout=5)
        output, error = await result.communicate()
        if result.returncode == 0:
            return {'status': 'completed', 'output': output}
        else:
            return {'status': 'failed', 'error': error}
    except subprocess.TimeoutExpired:
        return {'status': 'timeout', 'message': 'Ping request timed out'}

@app.get('/ping')
def ping(host: str):
    return safe_ping(host)