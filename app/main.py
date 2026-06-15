from fastapi import FastAPI
import subprocess
class PingCommand:
    def __init__(self, host):
        self.host = host

    async def execute(self):
        try:
            args = ['ping', self.host]  # Directly pass the host without shlex.quote()
            output = await asyncio.create_subprocess_exec(*args, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            result, error = await output.communicate()
            if output.returncode != 0:
                return {'status': 'failed', 'error': error.decode()}
            else:
                return {'status': 'completed', 'output': result.decode()}
        except Exception as e:
            return {'status': 'failed', 'error': str(e)}

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    return PingCommand(host).execute()