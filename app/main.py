from fastapi import FastAPI
import subprocess
import shlex
class SafePing:
    def __init__(self):
        pass

    async def ping(self, host: str):
        try:
            command = f'ping {host}'
            args = shlex.split(command)
            result = await asyncio.create_subprocess_exec(*args, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            output, error = await result.communicate()
            return {'status': 'completed', 'output': output.decode(), 'error': error.decode() if error else None}
        except Exception as e:
            return {'status': 'failed', 'message': str(e)}

app = FastAPI()
safe_ping = SafePing()

@app.get("/ping")
def ping(host: str):
    return safe_ping.ping(host)