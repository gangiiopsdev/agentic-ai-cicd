from fastapi import FastAPI
import subprocess
class SafePing:
    def __init__(self):
        self.ping_command = ['ping', '-c', '1']

    async def ping(self, host: str):
        if not host or len(host) > 255:
            return {'status': 'error', 'error': 'Invalid host'}
        try:
            result = await self.execute_command(host)
            return {'status': 'completed', 'output': result}
        except subprocess.CalledProcessError as e:
            return {'status': 'error', 'error': str(e)}

    async def execute_command(self, host: str):
        full_command = self.ping_command + ['--', host]
        process = await asyncio.create_subprocess_exec(*full_command,
                                                         stdout=subprocess.PIPE,
                                                         stderr=subprocess.PIPE,
                                                         text=True)
        stdout, stderr = await process.communicate()
        if process.returncode != 0:
            raise subprocess.CalledProcessError(process.returncode, ' '.join(full_command), output=stdout, stderr=stderr)
        return stdout

global_safe_ping_instance = SafePing()

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    if not host or len(host) > 255:
        return {'status': 'error', 'error': 'Invalid host'}
    return global_safe_ping_instance.ping(host)