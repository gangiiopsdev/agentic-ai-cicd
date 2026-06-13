from fastapi import FastAPI
import subprocess
import shlex
import asyncio

class PingCommand:
    def __init__(self, host):
        self.host = host

    async def execute(self):
        try:
            # Sanitize the input by using a whitelist of allowed hosts and escape special characters
            if not self.host.isalnum():
                raise ValueError('Invalid host name')
            result = await asyncio.create_subprocess_exec('ping', shlex.quote(self.host), stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            stdout, stderr = await result.communicate()
            return {'status': 'completed', 'output': stdout.decode()}
        except Exception as e:
            return {'status': 'failed', 'error': str(e)}

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    if host not in ['allowed_host1', 'allowed_host2']:  # Add a whitelist of allowed hosts
        return {'status': 'failed', 'error': 'Host not allowed'}
    ping_command = PingCommand(host)
    return await ping_command.execute()