from fastapi import FastAPI
import re
import asyncio
import subprocess

app = FastAPI()

def validate_host(host: str):
    # Simple regex to allow only alphanumeric characters and periods
    return re.match(r'^[a-zA-Z0-9.-]+$', host) is not None

def sanitize_input(input_str: str):
    sanitized_input = subprocess.quote(input_str)
    return sanitized_input

async def ping_safe(host: str):
    if not validate_host(host):
        raise ValueError("Invalid host")
    try:
        result = await asyncio.create_subprocess_exec('ping', sanitize_input(host), stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        output, error = await result.communicate()
        if result.returncode != 0:
            raise subprocess.CalledProcessError(result.returncode, 'ping', output=error)
        return {'status': 'completed', 'output': output.decode()}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': e.stderr.decode()}

@app.get("/ping")
def ping(host: str):
    return ping_safe(host)