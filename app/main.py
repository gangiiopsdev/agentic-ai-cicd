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
            return {'status': 'completed', 'output': output.stdout.decode()}
        except Exception as e:
            return {'status': 'error', 'error': str(e)}

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    if not is_valid_host(host):
        return {'status': 'error', 'error': 'Invalid host'}
    return PingCommand(host).execute()
def is_valid_host(host):
    # Add validation logic here, e.g., checking for IP address format or domain name validity
    return True