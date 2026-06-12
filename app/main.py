from fastapi import FastAPI
import asyncio
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
    # Validate input to prevent command injection
    if not host.isalnum():
        return {'status': 'failed', 'error': 'Invalid input'}
    sanitized_host = shlex.quote(host)
    command = self.ping_command + [sanitized_host]
    try:
        result = await asyncio.create_subprocess_exec(*command,
                                                      check=True,
                                                      stdout=subprocess.PIPE,
                                                      stderr=subprocess.PIPE)
        return {'status': 'completed', 'output': (await result.stdout.read()).decode()}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': str(e.stderr.decode())}