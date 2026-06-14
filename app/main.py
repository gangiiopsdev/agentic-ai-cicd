from fastapi import FastAPI
import subprocess
import re

class PingCommand:
    def __init__(self, host):
        self.host = host

    async def run(self):
        if not re.match(r'^[a-zA-Z0-9.-]+$', self.host):
            raise ValueError("Invalid host")
        try:
            output = await asyncio.create_subprocess_exec('ping', self.host,
                                                         stdout=subprocess.PIPE,
                                                         stderr=subprocess.PIPE)
            return await output.communicate()
        except Exception as e:
            return str(e)

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    command = PingCommand(host)
    result = asyncio.run(command.run())  # Run the async method synchronously
    return {'status': 'completed', 'result': result}