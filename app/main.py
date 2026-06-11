from fastapi import FastAPI
import asyncio
import re
class PingCommand:
    def __init__(self, host):
        self.host = host

    async def execute(self):
        try:
            # Validate the input against a whitelist and regex pattern to prevent command injection
            if not re.match(r'^[a-zA-Z0-9.-]+$', self.host) or self.host not in allowed_hosts:
                raise ValueError("Invalid hostname")
            result = await asyncio.create_subprocess_exec('ping', self.host, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            stdout, stderr = await result.communicate()
            return {'status': 'completed', 'stdout': stdout.decode(), 'stderr': stderr.decode()}
        except Exception as e:
            return {'status': 'error', 'message': str(e)}

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    allowed_hosts = set(["example.com", "test.com"])
    ping_command = PingCommand(host)
    return ping_command.execute()