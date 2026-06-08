from fastapi import FastAPI
import asyncio

class PingService:
    def __init__(self):
        self.ping_command = ['ping', '-c', '4']

    async def ping(self, host: str):
        try:
            result = await self._run_subprocess([*self.ping_command, f'-{host}'])
            return {'status': 'completed', 'output': result.stdout}
        except subprocess.CalledProcessError as e:
            return {'status': 'failed', 'error': e.stderr.decode()}

    async def _run_subprocess(self, cmd):
        process = await asyncio.create_subprocess_exec(*cmd,
                                                     stdout=subprocess.PIPE,
                                                     stderr=subprocess.PIPE)
        stdout, stderr = await process.communicate()
        if process.returncode != 0:
            raise subprocess.CalledProcessError(process.returncode, cmd, output=stdout.decode(), stderr=stderr.decode())
        return {'stdout': stdout.decode(), 'stderr': stderr.decode()}

app = FastAPI()
ping_service = PingService()

@app.get('/ping/{host}')
def ping_route(host: str):
    return await ping_service.ping(f'-{host}')