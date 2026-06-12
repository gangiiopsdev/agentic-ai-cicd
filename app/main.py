from fastapi import FastAPI
import subprocess
import shlex

class App:
    def __init__(self):
        self.app = FastAPI()

    async def ping_route(self, host: str):
        args = ['ping', *shlex.split(host)]
        result = await self._run_subprocess(args)
        return {'result': result}

    async def _run_subprocess(self, cmd: list):
        process = await asyncio.create_subprocess_exec(*cmd,
                                                       stdout=subprocess.PIPE,
                                                       stderr=subprocess.PIPE)
        stdout, stderr = await process.communicate()
        return stdout.decode() if process.returncode == 0 else str(stderr)

app = App().app