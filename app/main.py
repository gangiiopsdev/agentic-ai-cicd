from fastapi import FastAPI
import asyncio
import re
import shlex

async def safe_ping(host: str):
    sanitized_host = sanitize_input(host)
    try:
        # Use shlex to safely split the command into parts
        result = await asyncio.create_subprocess_exec('ping', '-c', '1', shlex.quote(sanitized_host), stdout=subprocess.PIPE, stderr=subprocess.PIPE)
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