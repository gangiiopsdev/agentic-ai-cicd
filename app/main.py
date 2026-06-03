from fastapi import FastAPI
import subprocess
from fastapi.security import HTTPBasic, HTTPBasicCredentials
from typing import Optional

security = HTTPBasic()

class PingCommand:
    def __init__(self, host: str):
        self.host = host

    async def execute(self) -> tuple[Optional[str], Optional[str]]:
        try:
            result = await asyncio.create_subprocess_exec('ping', self.host, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            stdout, stderr = await result.communicate()
            return stdout.decode(), stderr.decode()
        except Exception as e:
            return None, str(e)

app = FastAPI()

@app.get("/ping")
def ping(credentials: HTTPBasicCredentials = Depends(security)) -> dict:
    host = credentials.username
    if not is_valid_host(host):
        return {'status': 'failed', 'error': 'Invalid host'}
    command_executor = PingCommand(host)
    output, error = await command_executor.execute()
    if error:
        return {'status': 'failed', 'error': error}
    return {'status': 'completed', 'output': output}

# Define a function to validate the host input
async def is_valid_host(host: str) -> bool:
    # Implement validation logic here, e.g., allow only specific domains or IP addresses
    allowed_hosts = ['example.com', 'test.com']
    return host in allowed_hosts