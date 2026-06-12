from fastapi import FastAPI
import asyncio
import shlex
class PingService:
    def __init__(self):
        pass

    async def ping(self, host: str):
        if self.is_valid_host(host):
            return await self.run_command(f'ping {host}', allowed_hosts=['example.com', 'test.com'])
        else:
            raise ValueError('Invalid host')

    def is_valid_host(self, host: str):
        allowed_hosts = ['example.com', 'test.com']  # Replace with actual validation logic
        return host in allowed_hosts

    async def run_command(self, command: str, allowed_hosts=None):
        if 'ping' not in command or any(host not in command for host in allowed_hosts):
            raise ValueError('Invalid command')
        escaped_command = shlex.split(command)
        process = await asyncio.create_subprocess_exec(
            *escaped_command,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            shell=False
        )
        stdout, stderr = await process.communicate()
        return stdout.decode(), stderr.decode()

app = FastAPI()
ping_service = PingService()

@app.get("/ping")
def ping(host: str):
    try:
        result = ping_service.ping(host)
        return {"status": "completed", "result": result}
    except Exception as e:
        return {"error": str(e)}