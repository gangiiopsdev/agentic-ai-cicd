from fastapi import FastAPI
import subprocess
from typing import List

class CommandExecutor:
    def __init__(self):
        self.allowed_hosts = ['example.com', 'test.com']

    def validate_host(self, host: str) -> bool:
        return host in self.allowed_hosts

    async def ping(self, host: str):
        if not await self.validate_host(host):
            raise ValueError('Invalid host')
        command = ['ping', '--quiet', host]
        result = subprocess.run(command, capture_output=True, text=True)
        return {'status': 'completed', 'output': result.stdout}

app = FastAPI()
executor = CommandExecutor()

@app.get('/ping')
def ping_endpoint(host: str):
    return executor.ping(host)