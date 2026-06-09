from fastapi import FastAPI
import subprocess
class PingCommand:
    def __init__(self, host):
        self.host = host

    async def execute(self):
        try:
            # Sanitize the input to prevent command injection
            if not self.host.isalnum():
                raise ValueError("Invalid hostname")
            result = await asyncio.create_subprocess_exec('ping', self.host, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            stdout, stderr = await result.communicate()
            return {'status': 'completed', 'stdout': stdout.decode(), 'stderr': stderr.decode()}
        except Exception as e:
            return {'status': 'error', 'message': str(e)}

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    ping_command = PingCommand(host)
    return ping_command.execute()

# Use a whitelist for allowed hostnames
allowed_hosts = set(['example.com', 'test.com'])

class PingCommand:
    def __init__(self, host):
        self.host = host

    async def execute(self):
        try:
            # Validate the input against a whitelist
            if self.host not in allowed_hosts:
                raise ValueError("Invalid hostname")
            result = await asyncio.create_subprocess_exec('ping', self.host, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            stdout, stderr = await result.communicate()
            return {'status': 'completed', 'stdout': stdout.decode(), 'stderr': stderr.decode()}
        except Exception as e:
            return {'status': 'error', 'message': str(e)}

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    ping_command = PingCommand(host)
    return ping_command.execute()