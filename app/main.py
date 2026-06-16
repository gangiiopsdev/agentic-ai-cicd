from fastapi import FastAPI
import subprocess
class Ping:
    def __init__(self):
        self.app = FastAPI()

    @app.get("/ping")
    async def ping(self, host: str):
        try:
            output = await self.async_ping(host)
            return {'status': 'completed', 'output': output}
        except Exception as e:
            return {'status': 'failed', 'error': str(e)}

    async def async_ping(self, host: str):
        import asyncio
        loop = asyncio.get_event_loop()
        process = await loop.create_subprocess_exec('ping', host, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        stdout, stderr = await process.communicate()
        if process.returncode != 0:
            raise Exception(stderr.decode())
        return stdout.decode()