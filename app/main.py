from fastapi import FastAPI
import asyncio
import shlex
class PingCommand:
    def __init__(self, host: str):
        self.host = host

    async def execute(self):
        args = ['ping', *shlex.split(shlex.quote(self.host))]
        return await asyncio.create_subprocess_exec(*args)
def validate_host(host: str) -> bool:
    # Basic validation to ensure the host is a valid IP address or hostname
    import re
    pattern = r'^[a-zA-Z0-9.-]+$'
    return re.match(pattern, host) is not None
cmd_blacklist = [';', '&', '|', '(', ')', '<', '>', '*', '?', '~', '`']
def validate_command(host: str) -> bool:
    for char in cmd_blacklist:
        if char in host:
            return False
    return True

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    if validate_host(host) and validate_command(host):
        command = PingCommand(host)
        result = await command.execute()
        return {"status": "completed", "result": result}
    else:
        return {"error": "Invalid host input."}