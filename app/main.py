from fastapi import FastAPI
import subprocess
class PingCommand:
    def __init__(self, host):
        self.host = host

    async def execute(self):
        try:
            result = await asyncio.create_subprocess_exec('ping', self.host, stdout=asyncio.subprocess.PIPE, stderr=asyncio.subprocess.PIPE)
            output, error = await result.communicate()
            if result.returncode != 0:
                raise Exception(f'Ping failed: {error.decode()}')
            return {'status': 'completed'}
        except Exception as e:
            return {'status': 'failed', 'message': str(e)}

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    ping_command = PingCommand(host)
    return ping_command.execute()