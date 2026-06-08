from fastapi import FastAPI
import subprocess
class PingCommand:
    def __init__(self, host):
        self.host = host

    async def execute(self):
        result = await asyncio.create_subprocess_exec('ping', self.host, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        stdout, stderr = await result.communicate()
        return stdout.decode(), stderr.decode()

class PingEndpoint:
    @app.get("/ping")
    async def ping(host: str):
        ping_command = PingCommand(host)
        status, error = await ping_command.execute()
        if error:
            return {"status": "error", "error": error}
        else:
            return {"status": "completed", "stdout": status}