from fastapi import FastAPI
import subprocess
from fastapi.responses import HTTPException
class CommandExecutor:
    def __init__(self):
        self.allowed_hosts = ['google.com', 'example.com']

    def is_safe_host(self, host):
        return host in self.allowed_hosts

    async def execute_command(self, command, host=None):
        if host and not self.is_safe_host(host):
            raise HTTPException(status_code=403, detail="Invalid host")
        subprocess.run(command.split(), shell=False, check=True)

app = FastAPI()
executor = CommandExecutor()

@app.get("/ping")
def ping(host: str):
    command = f"ping {host}"
    await executor.execute_command(command, host=host)
    return {"status": "completed"}