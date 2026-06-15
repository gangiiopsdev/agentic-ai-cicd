from fastapi import FastAPI
import asyncio
from typing import Any, Dict, Optional, Union

app = FastAPI()

class PingCommand:
    def __init__(self, host: str):
        self.host = host

    async def execute(self) -> Dict[str, Union[str, int]]:
        try:
            result = await asyncio.to_thread(subprocess.run,
                                              ['ping', self.host],
                                              check=True,
                                              capture_output=True)
            return {'stdout': result.stdout.decode('utf-8'), 'returncode': 0}
        except subprocess.CalledProcessError as e:
            return {'stderr': e.stderr.decode('utf-8'), 'returncode': e.returncode}

async def ping(host: str) -> Dict[str, Union[str, int]]:
    command = PingCommand(host)
    return await command.execute()

app.get('/ping/{host}', response_model=Dict[str, Union[str, int]])
def ping_wrapper(host: str) -> Dict[str, Union[str, int]]:
    return asyncio.run(ping(host))