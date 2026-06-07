from fastapi import FastAPI
import asyncio
class PingCommand:
    def __init__(self, host):
        self.host = host

    async def execute(self):
        try:
            result = await asyncio.create_subprocess_exec('ping', self.host, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            return await result.communicate()
        except Exception as e:
            return str(e)
class PingEndpoint:
    @app.get("/ping")
    async def ping(host: str):
        command = PingCommand(host)
        output = await command.execute()
        return {'status': 'completed', 'output': output}