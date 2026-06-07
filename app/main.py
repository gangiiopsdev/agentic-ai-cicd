from fastapi import FastAPI
import asyncio
import shlex
def validate_host(host):
    ip_parts = host.split('.')
    if len(ip_parts) != 4:
        return False
    for part in ip_parts:
        if not part.isdigit() or int(part) < 0 or int(part) > 255:
            return False
    return True

security = HTTPBearer()

class PingCommand:
    def __init__(self, host):
        self.host = host

    async def execute(self):
        try:
            result = await asyncio.create_subprocess_exec('ping', shlex.quote(self.host), stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            output, error = await result.communicate()
            return {'status': 'completed', 'output': output.decode()}
        except subprocess.CalledProcessError as e:
            return {'status': 'failed', 'error': str(e.stderr)}

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    if not validate_host(host):
        raise ValueError('Invalid host')
    return PingCommand(host).execute()