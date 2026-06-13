from fastapi import FastAPI
import asyncio
from typing import List

class PingService:
    def __init__(self):
        pass

    async def ping(self, host: str):
        if self.is_valid_host(host):
            return await self.run_command(f'ping {host}', allowed_hosts=['example.com', 'test.com'])
        else:
            raise ValueError('Invalid host')

    def is_valid_host(self, host: str) -> bool:
        allowed_hosts = ['example.com', 'test.com']  # Replace with actual validation logic
        return host in allowed_hosts

    async def run_command(self, command: str, allowed_hosts: List[str] = None):
        if not self.is_allowed_command(command, allowed_hosts):
            raise ValueError('Invalid command')
        process = await asyncio.create_subprocess_exec(
            *command.split(),
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            shell=False
        )
        stdout, stderr = await process.communicate()
        return stdout.decode(), stderr.decode()

    def is_allowed_command(self, command: str, allowed_hosts: List[str]) -> bool:
        if 'ping' not in command:
            return False
        for host in allowed_hosts or []:
            if host not in command:
                return False
        return True

app = FastAPI()
ping_service = PingService()

@app.get("/ping")
def ping(host: str):
    try:
        result = ping_service.ping(host)
        return {"status": "completed", "result": result}
    except Exception as e:
        return {"error": str(e)}