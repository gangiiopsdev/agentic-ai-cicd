from fastapi import FastAPI
import subprocess
class PingCommand:
    def __init__(self, host):
        self.host = host

    async def execute(self):
        try:
            result = await asyncio.create_subprocess_shell(f'ping {self.host}', stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            stdout, stderr = await result.communicate()
            return {'status': 'completed', 'stdout': stdout.decode(), 'stderr': stderr.decode()}
        except Exception as e:
            return {'status': 'failed', 'error': str(e)}

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    command = PingCommand(host)
    return command.execute()