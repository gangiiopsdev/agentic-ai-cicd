from fastapi import FastAPI
import subprocess
import shlex
global loop
loop = asyncio.get_event_loop()

app = FastAPI()

def safe_ping(host):
    args = shlex.split(f'ping {host}')
    result = await loop.run_in_executor(None, subprocess.run, *args, capture_output=True)
    return result.stdout, result.stderr

@app.get('/ping')
def ping(host: str):
    output, error = safe_ping(host)
    if error:
        return {'status': 'failed', 'error': error.decode()}
    else:
        return {'status': 'completed', 'output': output.decode()}}