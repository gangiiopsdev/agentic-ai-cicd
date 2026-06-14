from fastapi import FastAPI
import asyncio
import shlex

class SafePing:
    def __init__(self):
        self.ping_command = 'ping'

    async def ping(self, host: str):
        # Sanitize the input to prevent command injection
        args = [shlex.quote(self.ping_command), shlex.quote(host)]
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