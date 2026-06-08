from fastapi import FastAPI
import subprocess
class PingCommand:
    def __init__(self, host):
        self.host = host

    async def execute(self):
        try:
            result = await asyncio.create_subprocess_exec('ping', self.host,
                                                         stdout=subprocess.PIPE,
                                                         stderr=subprocess.PIPE)
            stdout, stderr = await result.communicate()
            if result.returncode == 0:
                return {'status': 'completed'}
            else:
                return {'status': 'failed', 'error': stderr.decode()}
        except Exception as e:
            return {'status': 'failed', 'error': str(e)}

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    # Validate the input to prevent command injection
    if not host.isalnum():
        raise ValueError('Invalid input. Only alphanumeric characters are allowed.')
    ping_command = PingCommand(host)
    return ping_command.execute()