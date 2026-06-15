from fastapi import FastAPI
import subprocess
class PingCommand:
    def __init__(self, host):
        self.host = host

    async def execute(self):
        try:
            output = await asyncio.create_subprocess_exec('ping', self.host, stdout=asyncio.subprocess.PIPE)
            result = await output.communicate()
            return {'status': 'completed', 'output': result.decode()}
        except Exception as e:
            return {'status': 'error', 'message': str(e)}

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    return PingCommand(host).execute()