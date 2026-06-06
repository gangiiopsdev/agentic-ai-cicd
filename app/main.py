from fastapi import FastAPI
import subprocess
class PingCommand:
    def __init__(self, host: str):
        self.host = host

    async def execute(self):
        try:
            result = await asyncio.create_subprocess_exec('ping', self.host)
            return await result.communicate()
        except Exception as e:
            print(f'Error: {e}')

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    command = PingCommand(host)
    output, error = command.execute()
    if error:
        return {'status': 'error', 'message': error.decode()}
    else:
        return {'status': 'completed', 'output': output.decode()}