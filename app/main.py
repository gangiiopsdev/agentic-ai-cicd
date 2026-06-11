from fastapi import FastAPI
import asyncio
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
class PingCommand:
    def __init__(self, host):
        self.host = host

    async def execute(self):
        try:
            result = await asyncio.create_subprocess_exec('ping', self.host, stdout=asyncio.subprocess.PIPE, stderr=asyncio.subprocess.PIPE)
            output, error = await result.communicate()
            if result.returncode != 0:
                raise Exception(f'Ping failed: {error.decode()}')
            return {'status': 'completed'}
        except Exception as e:
            return {'status': 'failed', 'message': str(e)}

app = FastAPI()
bearer_scheme = HTTPBearer()
@app.get("/ping")
def ping(host: str, credentials: HTTPAuthorizationCredentials = Depends(bearer_scheme)):
    if credentials.credentials == "secret":  # Replace with actual authentication logic
        return PingCommand(host).execute()
    else:
        return {'status': 'failed', 'message': 'Unauthorized'}

# Sanitize input to prevent command injection
import re
def sanitize_host(host):
    if re.match(r'^[a-zA-Z0-9.-]+$', host):
        return host
    raise ValueError("Invalid hostname")

@app.get("/ping_sanitize")
def ping_sanitize(host: str, credentials: HTTPAuthorizationCredentials = Depends(bearer_scheme)):
    if credentials.credentials == "secret":  # Replace with actual authentication logic
        sanitized_host = sanitize_host(host)
        return PingCommand(sanitized_host).execute()
    else:
        return {'status': 'failed', 'message': 'Unauthorized'}