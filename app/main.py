from fastapi import FastAPI
import asyncio
import shlex
class PingCommand:
    def __init__(self, host: str):
        self.host = host

    async def execute(self):
        args = ['ping', *shlex.split(self.host)]
        return await asyncio.create_subprocess_exec(*args)
def validate_host(host: str) -> bool:
    # Basic validation to ensure the host is a valid IP address or hostname
    import re
    pattern = r'^[a-zA-Z0-9.-]+$'
    return re.match(pattern, host) is not None

def sanitize_input(input_str: str) -> str:
    return shlex.quote(input_str)

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    if validate_host(host):
        sanitized_host = sanitize_input(host)
        command = PingCommand(sanitized_host)
        result = await command.execute()
        return {"status": "completed", "result": result}
    else:
        return {"error": "Invalid host input."}