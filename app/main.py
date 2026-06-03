from fastapi import FastAPI
import subprocess
import shlex

class PingCommand:
    def __init__(self, host):
        self.host = host

    async def execute(self):
        try:
            args = ['ping', self.host]
            result = await asyncio.create_subprocess_exec(*args, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            output, error = await result.communicate()
            return {'status': 'completed', 'output': output.decode()}
        except subprocess.CalledProcessError as e:
            return {'status': 'failed', 'error': str(e.stderr)}

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    # Sanitize the input to prevent command injection
    sanitized_host = shlex.quote(host)
    return PingCommand(sanitized_host).execute()