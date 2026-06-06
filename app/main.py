from fastapi import FastAPI
import asyncio
import shlex

class PingCommand:
    def __init__(self, host):
        self.host = host

    async def execute(self):
        try:
            output = await asyncio.create_subprocess_exec('ping', *shlex.split(self.host), capture_output=True, text=True)
            return output.stdout
        except Exception as e:
            return str(e.output.decode('utf-8'))

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    ping_command = PingCommand(host)
    result = await ping_command.execute()
    return {"status": "completed", "result": result}