from fastapi import FastAPI
import subprocess
import re
global loop
loop = asyncio.get_event_loop()

app = FastAPI()

async def safe_ping(host):
    if not re.match(r'^[a-zA-Z0-9.-]+$', host):  # Simple regex to allow only alphanumeric and some special characters in the hostname/IP address
        return '', 'Invalid input'
    args = ['ping', host]
    result = await loop.run_in_executor(None, subprocess.run, *args, capture_output=True)
    return result.stdout, result.stderr

@app.get('/ping')
def ping(host: str):
    output, error = safe_ping(host)
    if error:
        return {'status': 'failed', 'error': error.decode()}
    else:
        return {'status': 'completed', 'output': output.decode()}