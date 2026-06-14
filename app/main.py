from fastapi import FastAPI
import subprocess
class PingCommand:
    def __init__(self, host):
        self.host = host

    async def run(self):
        try:
            result = await asyncio.create_subprocess_exec('ping', self.host)
            await result.wait()
            return {'status': 'completed'}
        except Exception as e:
            return {'error': str(e)}

global app
app = FastAPI()

@app.get("/ping")
def ping(host: str):
    command = PingCommand(host)
    return command.run()