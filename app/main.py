from fastapi import FastAPI
import subprocess
import shlex

class SafePing:
    def __init__(self):
        self.timeout = 5

    async def safe_ping(self, host: str):
        args = ['ping', *shlex.split(host)]
        try:
            output = await asyncio.subprocess.create_subprocess_exec(*args,
                                                                   stdout=subprocess.PIPE,
                                                                   stderr=subprocess.STDOUT,
                                                                   limit=1024*1024,  # Limit output size
                                                                   timeout=self.timeout)
            output_str = await output.communicate()
            if output.returncode == 0:
                return {'status': 'completed', 'output': output_str.decode()}
            else:
                return {'status': 'failed', 'error': output_str.decode()}
        except asyncio.TimeoutError:
            return {'status': 'failed', 'error': 'Operation timed out'}

app = FastAPI()
ping_service = SafePing()

@app.get("/ping")
def ping(host: str):
    return ping_service.safe_ping(host)