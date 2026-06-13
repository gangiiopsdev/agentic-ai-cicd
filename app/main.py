from fastapi import FastAPI
import subprocess
import shlex
class SanitizedPing:
    def __init__(self):
        pass

    async def ping(self, host: str):
        # Sanitize the input to avoid command injection
        args = ['ping', shlex.quote(host)]
        result = await asyncio.create_subprocess_exec(*args,
                                               stdout=subprocess.PIPE,
                                               stderr=subprocess.PIPE)
        output, error = await result.communicate()
        if result.returncode != 0:
            return {'status': 'failed', 'error': error.decode()}
        return {'status': 'completed', 'output': output.decode()}

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    ping_service = SanitizedPing()
    return ping_service.ping(host)