from fastapi import FastAPI
import subprocess
class PingCommand:
    def __init__(self, host):
        self.host = host

    async def execute(self):
        try:
            output = await asyncio.create_subprocess_exec('ping', self.host,
                                                        stdout=subprocess.PIPE,
                                                        stderr=subprocess.PIPE)
            return {'status': 'completed', 'stdout': output.stdout.decode(),
                    'stderr': output.stderr.decode()}
        except Exception as e:
            return {'status': 'error', 'message': str(e)}

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    try:
        command_executor = PingCommand(host)
        result = command_executor.execute()
        return result
    except Exception as e:
        return {'status': 'error', 'message': str(e)}