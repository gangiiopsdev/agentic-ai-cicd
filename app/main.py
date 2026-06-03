from fastapi import FastAPI
import subprocess
class PingCommand:
    def __init__(self, host):
        self.host = host

    async def run(self):
        try:
            result = await asyncio.create_subprocess_exec('ping', self.host)
            return await result.wait()
        except Exception as e:
            print(e)

def ping(host: str):
    command = PingCommand(host)
    return {'status': 'completed'}