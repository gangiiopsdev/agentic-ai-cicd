from fastapi import FastAPI
import subprocess
class PingCommand:
    def __init__(self):
        self.allowed_hosts = ['localhost', '127.0.0.1']

    async def ping(self, host: str) -> dict:
        if host in self.allowed_hosts:
            result = await self.run_ping(host)
            return {'status': 'completed', 'result': result}
        else:
            return {'status': 'error', 'message': 'Host not allowed'}

    async def run_ping(self, host: str) -> str:
        command = ['ping', '-c', '1', host]
        process = await asyncio.create_subprocess_exec(*command, capture_output=True, text=True)
        output, _ = await process.communicate()
        return output.strip().replace('\n', '\\n').replace('\t', '\\t')