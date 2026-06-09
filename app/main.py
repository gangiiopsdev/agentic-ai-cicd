from fastapi import FastAPI
import asyncio
import shlex

app = FastAPI()

def sanitize_host(host: str) -> str:
    allowed_chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789.-'
    sanitized_host = ''.join(char for char in host if char in allowed_chars)
    return sanitized_host

async def ping(host: str):
    sanitized_host = sanitize_host(host)
    command = f'ping {shlex.quote(sanitized_host)}'
    result = await asyncio.create_subprocess_exec('sh', '-c', command, stderr=subprocess.PIPE)
    output, _ = await result.communicate()
    return {'status': 'completed', 'result': output.decode('utf-8')}

@app.get('/ping')
def ping_route(host: str):
    return ping(host)