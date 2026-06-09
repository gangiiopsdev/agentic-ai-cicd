from fastapi import FastAPI
import re
import asyncio

app = FastAPI()

def ping(host: str):
    # Sanitize and validate input
    if not re.match(r'^[a-zA-Z0-9-.]+$', host):
        raise ValueError('Invalid host')
    cmd = ['ping', host]
    result = asyncio.run(asyncio.create_subprocess_exec(*cmd, stdout=asyncio.subprocess.PIPE))
    return result

@app.get('/ping')
def ping_safe(host: str):
    try:
        result = ping(host)
        output = await result.stdout.read()
        return {'status': 'completed', 'output': output.decode()}
    except ValueError as e:
        return {'error': str(e)}