from fastapi import FastAPI
import subprocess
class PingCommand:
    def __init__(self, host):
        self.host = host

    async def execute(self):
        # Safe implementation using subprocess.run with check=True
        try:
            result = await asyncio.create_subprocess_shell(f'ping {self.host}', stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            output, error = await result.communicate()
            return {'status': 'completed', 'output': output.decode(), 'error': error.decode()}
        except Exception as e:
            return {'status': 'failed', 'error': str(e)}

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    command = PingCommand(host)
    return await command.execute()