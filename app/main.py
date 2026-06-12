from fastapi import FastAPI
import re
from typing import Optional

app = FastAPI()

async def safe_ping(host: str) -> str:
    if not re.match(r'^[a-zA-Z0-9.-]+$', host):
        raise ValueError("Invalid host input")
    try:
        output = await asyncio.create_subprocess_exec('ping', host, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        stdout, stderr = await output.communicate()
        if output.returncode != 0:
            return stderr.decode('utf-8')
        return stdout.decode('utf-8')
    except subprocess.CalledProcessError as e:
        return str(e)

@app.get('/ping')
def ping(host: Optional[str] = None):
    if not host:
        raise ValueError("Host parameter is required")
    return {'status': 'completed', 'output': await safe_ping(host)}