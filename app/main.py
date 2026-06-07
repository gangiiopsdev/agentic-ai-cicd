from fastapi import FastAPI
import subprocess
from fastapi.responses import HTTPException
import shlex

class CommandExecutor:
    def __init__(self):
        self.allowed_hosts = ['google.com', 'example.com']

    def is_safe_host(self, host):
        return host in self.allowed_hosts

    async def execute_command(self, command, host=None):
        if host and not self.is_safe_host(host):
            raise HTTPException(status_code=403, detail="Invalid host")
        args = shlex.split(command)
        subprocess.run(args, check=True)

app = FastAPI()
executor = CommandExecutor()

@app.get("/ping")
def ping(host: str):  # Ensure input is sanitized to prevent command injection
    if ' ' in host or not host.isalnum():  # Simple input validation
        raise HTTPException(status_code=403, detail="Invalid input")
    command = f"ping {host}"
    await executor.execute_command(command, host=host)
    return {"status": "completed"}