from fastapi import FastAPI
import subprocess
class PingCommand:
    def __init__(self, host: str):
        self.host = host

    async def execute(self):
        return await asyncio.create_subprocess_exec('ping', self.host)

def validate_host(host: str) -> bool:
    # Basic validation to ensure the host is a valid IP address or hostname
    import re
    pattern = r'^[a-zA-Z0-9.-]+$'
    return re.match(pattern, host) is not None

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    if validate_host(host):
        command = PingCommand(host)
        result = await command.execute()
        return {"status": "completed", "result": result}
    else:
        return {"error": "Invalid host input."}