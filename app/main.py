from fastapi import FastAPI
import subprocess
class PingCommand:
    def __init__(self, host):
        self.host = host

    async def execute(self):
        try:
            sanitized_host = subprocess.quote(self.host)
            result = await asyncio.create_subprocess_exec('ping', sanitized_host,
                                                         stdout=subprocess.PIPE,
                                                         stderr=subprocess.PIPE)
            output, error = await result.communicate()
            return {'status': 'completed', 'output': output.decode(), 'error': error.decode() if error else None}
        except Exception as e:
            return {'status': 'failed', 'error': str(e)}

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    ping_command = PingCommand(host)
    return ping_command.execute()