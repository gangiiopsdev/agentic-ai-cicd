from fastapi import FastAPI
import subprocess
class PingCommand:
    def __init__(self, host):
        self.host = host

    async def execute(self):
        # Safe implementation
        try:
            result = await asyncio.create_subprocess_shell(
                f'ping {shlex.quote(self.host)}',
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE
            )
            return {'status': 'completed'}
        except Exception as e:
            return {'error': str(e)}

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    command = PingCommand(host)
    return await command.execute()