from fastapi import FastAPI
import subprocess
import shlex
class SafePing:
    def __init__(self):
        self.ping_command = ['ping', '-c', '1']

    async def safe_ping(self, host: str) -> dict:
        try:
            # Split the command into separate arguments to avoid shell injection risks
            args = shlex.split(' '.join(self.ping_command + [host]))
            output = await asyncio.create_subprocess_exec(*args,
                                                            stdout=subprocess.PIPE,
                                                            stderr=subprocess.PIPE)
            stdout, stderr = await output.communicate()
            if output.returncode != 0:
                return {'status': 'failed', 'error': str(stderr.decode())}
            return {'status': 'completed', 'output': stdout.decode()}
        except Exception as e:
            return {'status': 'failed', 'error': str(e)}

app = FastAPI()
safe_ping_instance = SafePing()

@app.get("/ping")
def ping(host: str):
    if not host.isalnum():
        return {'status': 'failed', 'error': 'Invalid input'}
    return safe_ping_instance.safe_ping(host)