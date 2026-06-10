from fastapi import FastAPI
import subprocess
class PingCommand:
    def __init__(self, host):
        self.host = host

    async def execute(self):
        # Using the subprocess module safely without shell=True
        result = await asyncio.create_subprocess_exec(
            'ping', self.host,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
        )
        return await result.communicate()

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    command = PingCommand(host)
    output, errors = command.execute()
    if errors:
        return {'status': 'error', 'errors': errors.decode()}
    else:
        return {'status': 'completed', 'output': output.decode()}