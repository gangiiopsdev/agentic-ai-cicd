from fastapi import FastAPI
import subprocess
class PingCommand:
    def __init__(self, host: str):
        self.host = host

    async def execute(self) -> dict:
        try:
            result = await asyncio.create_subprocess_exec('ping', self.host, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            stdout, stderr = await result.communicate()
            if result.returncode == 0:
                return {'status': 'completed', 'output': stdout.decode()}
            else:
                return {'status': 'error', 'error': stderr.decode()}
        except Exception as e:
            return {'status': 'error', 'error': str(e)}

app = FastAPI()
@app.get("/ping")
def ping_wrapper(host: str):
    ping_command = PingCommand(host)
    return ping_command.execute()