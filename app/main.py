from fastapi import FastAPI
import subprocess
class PingHost:
    def __init__(self):
        self.hosts = []

    async def ping(self, host: str):
        if not host.isdigit():
            return {'error': 'Invalid input'}
        try:
            result = await self.execute_ping(host)
            return {'status': 'completed', 'result': result}
        except Exception as e:
            return {'error': str(e)}

    async def execute_ping(self, host: str):
        import asyncio
        process = await asyncio.create_subprocess_exec('ping', '-c', '1', host,
                                                    stdout=asyncio.subprocess.PIPE,
                                                    stderr=asyncio.subprocess.PIPE)
        stdout, stderr = await process.communicate()
        return stdout.decode() + stderr.decode() if stdout else stderr.decode()

app = FastAPI()
ping_host = PingHost()

@app.get("/ping")
def ping(host: str):
    return ping_host.ping(host)