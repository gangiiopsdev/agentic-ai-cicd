from fastapi import FastAPI
import asyncio

class SafePing:
    def __init__(self):
        self.ping_command = 'ping'

    async def ping(self, host: str):
        # Validate the input to prevent command injection
        if not all(c.isalnum() or c in ['.', '-', '_'] for c in host):
            raise ValueError('Invalid host name')
        args = [self.ping_command, host]
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