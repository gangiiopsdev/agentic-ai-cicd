from fastapi import FastAPI
import subprocess
import shlex

async def safe_ping(host):
    try:
        output = await asyncio.to_thread(subprocess.check_output, ['ping', shlex.quote(host)], stderr=subprocess.STDOUT)
        return output.decode('utf-8')
    except subprocess.CalledProcessError as e:
        return str(e.output)

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    # Validate the host input to prevent command injection
    if not is_valid_host(host):
        raise ValueError('Invalid host format')
    result = await safe_ping(host)
    return {'status': 'completed', 'result': result}

import re
async def is_valid_host(host):
    # Enhanced regex to validate host format (IP address or domain name)
    pattern = r'^(([a-zA-Z0-9]|[a-zA-Z0-9][a-zA-Z0-9\-]*[a-zA-Z0-9])\.)*([A-Za-z0-9]|[A-Za-z0-9][A-Za-z0-9\-]*[A-Za-z0-9])$'
    return bool(re.match(pattern, host))