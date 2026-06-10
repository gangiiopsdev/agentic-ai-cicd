from fastapi import FastAPI
import subprocess
class PingCommand:
    def __init__(self, host):
        self.host = host

    async def execute(self):
        try:
            result = await asyncio.create_subprocess_exec('ping', self.host,
                                                       stdout=subprocess.PIPE,
                                                       stderr=subprocess.PIPE)
            stdout, stderr = await result.communicate()
            return {'status': 'completed', 'output': stdout.decode()}
        except Exception as e:
            return {'status': 'error', 'error': str(e)}

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    command_executor = PingCommand(host)
    return command_executor.execute()