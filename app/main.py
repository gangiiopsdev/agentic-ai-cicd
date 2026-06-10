from fastapi import FastAPI
import subprocess
import shlex

class SafePing:
    def __init__(self):
        self.ping_command = ['ping', '-c', '4']

    async def ping(self, host: str) -> dict:
        command = self.ping_command + shlex.split(host)
        try:
            result = await asyncio.create_subprocess_exec(*command,
                                                          check=True,
                                                          stdout=subprocess.PIPE,
                                                          stderr=subprocess.PIPE)
            return {'status': 'completed', 'output': (await result.stdout.read()).decode()}
        except subprocess.CalledProcessError as e:
            return {'status': 'failed', 'error': str(e.stderr.decode())}

app = FastAPI()
safe_ping_instance = SafePing()

@app.get('/ping')
def ping(host: str):
    return safe_ping_instance.ping(host)