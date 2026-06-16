from fastapi import FastAPI
import subprocess
class PingCommand:
    def __init__(self, host):
        self.host = host

    async def execute(self):
        try:
            result = await asyncio.create_subprocess_exec('ping', self.host, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            output, error = await result.communicate()
            return {'status': 'completed' if result.returncode == 0 else 'failed', 'output': output.decode(), 'error': error.decode()}
        except Exception as e:
            return {'status': 'failed', 'error': str(e)}

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    if validate_host(host):
        ping_command = PingCommand(host)
        return ping_command.execute()
    else:
        return {'status': 'failed', 'error': 'Invalid host'}

def validate_host(host):
    # Add validation logic here, e.g., check if the host is in a allowed list
    return True