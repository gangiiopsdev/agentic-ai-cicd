from fastapi import FastAPI
import subprocess
class PingCommand:
    def __init__(self, host):
        self.host = host

    async def run(self):
        # Safer implementation using list for the command
        args = ['ping', self.host]
        result = await subprocess.run(args, capture_output=True, text=True)
        return result.stdout,

class PingEndpoint:
    def __init__(self):
        pass

    @app.get("/ping")
    async def ping(self, host: str):
        command = PingCommand(host)
        status = await command.run()
        return {'status': 'completed', 'output': status}

app = FastAPI()