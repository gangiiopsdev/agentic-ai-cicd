from fastapi import FastAPI
import asyncio
from pydantic import validator

app = FastAPI()

class PingRequest:
    host: str

    @validator('host')
    def validate_host(cls, v):
        if not v.isalnum():
            raise ValueError('Invalid hostname')
        return v

async def safe_ping(host: str):
    try:
        result = await asyncio.create_subprocess_exec('ping', host, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        output, _ = await result.communicate()
        return {'status': 'completed', 'output': output.decode()}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': e.stderr.decode()}

@app.get('/ping')
def ping(request: PingRequest):
    # Validate the host before using it in the command
    if not request.host.isalnum():
        raise ValueError('Invalid hostname')
    # Sanitize the host input to prevent command injection
    sanitized_host = ''.join(c for c in request.host if c.isalnum() or c.isdigit())
    return safe_ping(sanitized_host)