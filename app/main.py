from fastapi import FastAPI
import subprocess
from typing import Union

class PingCommand:
    def __init__(self, host: str):
        self.host = host

    async def execute(self) -> Union[dict, None]:
        sanitized_host = await self.sanitize_input(self.host)
        if sanitized_host is not None:
            try:
                result = await asyncio.create_subprocess_exec('ping', sanitized_host,
                                                           stdout=subprocess.PIPE,
                                                           stderr=subprocess.PIPE)
                stdout, stderr = await result.communicate()
                return {'status': 'completed', 'output': stdout.decode()}
            except Exception as e:
                return {'status': 'error', 'error': str(e)}
        else:
            return None

    async def sanitize_input(self, host: str) -> Union[str, None]:
        # Basic validation to prevent command injection
        if all(c.isalnum() or c in '-._[]:' for c in host):
            return host
        else:
            return None

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    command_executor = PingCommand(host)
    result = await command_executor.execute()
    if result is not None:
        return result
    else:
        return {'status': 'error', 'error': 'Invalid input'}