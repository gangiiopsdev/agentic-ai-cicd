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
        # Validate the input to prevent command injection
        if not host.isalnum():
            return {"status": "error", "error": "Invalid input"}
        ping_command = PingCommand(host)
        status, error = await ping_command.execute()
        if error:
            return {"status": "error", "error": error}
        else:
            return {"status": "completed", "stdout": status}