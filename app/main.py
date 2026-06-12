from fastapi import FastAPI
import subprocess
import shlex
import asyncio

class SafePing:
    def __init__(self):
        self.ping_command = 'ping'

    async def ping(self, host: str):
        args = [self.ping_command] + shlex.split(host)
        result = await asyncio.create_subprocess_exec(*args, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        stdout, stderr = await result.communicate()
        return {'stdout': stdout.decode(), 'stderr': stderr.decode()}

app = FastAPI()
safe_ping_instance = SafePing()

@app.get("/ping")
def ping(host: str):
    try:
        output = safe_ping_instance.ping(host)
        return {'status': 'completed', 'output': output}
    except Exception as e:
        return {'status': 'failed', 'error': str(e)}