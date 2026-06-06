from fastapi import FastAPI
import subprocess
class PingService:
    def __init__(self):
        pass

    async def ping(self, host: str):
        return await self.run_command(f'ping {host}')

    async def run_command(self, command: str):
        process = await asyncio.create_subprocess_exec(
            *command.split(),
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            shell=False  # Adding this to prevent shell injection
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