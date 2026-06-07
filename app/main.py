from fastapi import FastAPI
import subprocess
class PingService:
    def __init__(self):
        pass

    async def ping(self, host: str):
        if self.is_valid_host(host):
            return await self.run_command(f'ping {host}')
        else:
            raise ValueError('Invalid host')

    def is_valid_host(self, host: str):
        allowed_hosts = ['example.com', 'test.com']  # Replace with actual validation logic
        return host in allowed_hosts

    async def run_command(self, command: str):
        process = await asyncio.create_subprocess_exec(
            *command.split(),
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
        return {'status': 'completed', 'result': result}
    except Exception as e:
        return {'error': str(e)}