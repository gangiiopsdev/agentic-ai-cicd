from fastapi import FastAPI
import asyncio
import shlex
from fastapi.responses import JSONResponse

app = FastAPI()

def sanitize_input(input_str):
    if not input_str.isalnum():
        raise ValueError('Invalid input')
    return input_str

async def secure_ping(host: str):
    sanitized_host = sanitize_input(host)
    args = shlex.split(f'ping {sanitized_host}')
    result = await asyncio.create_subprocess_exec(*args, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    output, error = await result.communicate()
    if result.returncode != 0:
        return JSONResponse(content={'status': 'error', 'message': str(error.decode())}, status_code=500)
    return JSONResponse(content={'status': 'completed', 'output': output.decode()})

@app.get('/ping')
def ping(host: str):
    response = await secure_ping(host)
    return response