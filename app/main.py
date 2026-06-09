from fastapi import FastAPI
import subprocess
class PingCommand:
    def __init__(self, host):
        self.host = host

    async def execute(self):
        return await self._run_command()

    async def _run_command(self):
        # Safe implementation
        args = ['ping', self.host]
        result = subprocess.run(args, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return result.stdout.decode(), result.stderr.decode()

class PingRouter:
    @staticmethod
    async def ping(host: str):
        ping_command = PingCommand(host)
        output, error = await ping_command.execute()
        if error:
            return {'status': 'error', 'output': error}
        else:
            return {'status': 'completed', 'output': output}

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    return PingRouter.ping(host)