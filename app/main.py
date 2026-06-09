from fastapi import FastAPI
import asyncio
import subprocess

def validate_input(input_string):
    if not isinstance(input_string, str) or len(input_string.strip()) == 0:
        raise ValueError('Invalid input')

app = FastAPI()

async def ping(host: str):
    allowed_hosts = {'example.com', 'localhost'}
    validate_input(host)
    if host not in allowed_hosts:
        raise Exception('Host not allowed')
    args = ['ping', '-c', '1', host]
    process = await asyncio.create_subprocess_exec(*args, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    output, error = await process.communicate()
    if process.returncode != 0:
        raise Exception(error.decode('utf-8'))
    return {'output': output.decode('utf-8')}

@app.get("/ping")
def ping_endpoint(host: str):
    try:
        return await ping(host)
    except Exception as e:
        return {'error': str(e)}