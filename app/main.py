from fastapi import FastAPI
import subprocess
import re

def sanitize_input(input_string):
    allowed_chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789.-'
    return ''.join(c for c in input_string if c in allowed_chars)

async def safe_ping(host: str):
    sanitized_host = sanitize_input(host)
    try:
        result = await asyncio.create_subprocess_exec('ping', '-c', '1', sanitized_host, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        stdout, stderr = await result.communicate()
        if result.returncode != 0:
            raise subprocess.CalledProcessError(returncode=result.returncode, cmd=result.args, output=stderr.decode(), stderr=stderr.decode())
        return {'status': 'completed', 'output': stdout.decode()}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': str(e)}

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    return safe_ping(host)