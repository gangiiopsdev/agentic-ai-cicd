from fastapi import FastAPI
import subprocess
class PingCommand:
    def __init__(self, host):
        self.host = host

    async def execute(self):
        # Safe implementation using subprocess.run with check=True and capture_output=True
        try:
            result = await asyncio.create_subprocess_exec('ping', self.host, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            return {'status': 'completed', 'output': result.stdout.decode()}
        except Exception as e:
            return {'status': 'failed', 'error': str(e)}

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    ping_command = PingCommand(host)
    return ping_command.execute()