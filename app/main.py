from fastapi import FastAPI
import subprocess

class SafePing:
    def __init__(self):
        self.allowed_hosts = ['localhost', '127.0.0.1']

    async def ping(self, host: str):
        if host in self.allowed_hosts:
            command = ['ping', '-c', '4', host]
            process = await asyncio.create_subprocess_exec(*command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            stdout, stderr = await process.communicate()
            return stdout.decode(), stderr.decode()
        else:
            raise ValueError('Unauthorized host')

app = FastAPI()
ping_service = SafePing()

@app.get('/ping')
def ping(host: str):
    try:
        result, error = ping_service.ping(host)
        if error:
            return {'error': error}
        else:
            return {'status': 'completed', 'result': result}
    except ValueError as e:
        return {'error': str(e)}

# Import necessary libraries
import os
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer
security = HTTPBearer()

@app.get('/ping_secure')
def ping(host: str, credentials: HTTPAuthorizationCredentials = Depends(security)):
    if 'admin' not in credentials.credentials:
        return {'error': 'Unauthorized'}
    try:
        result, error = ping_service.ping(host)
        if error:
            return {'error': error}
        else:
            return {'status': 'completed', 'result': result}
    except ValueError as e:
        return {'error': str(e)}