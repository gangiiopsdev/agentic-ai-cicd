from fastapi import FastAPI
import asyncio
class PingCommand:
    def __init__(self, host):
        self.host = host

    async def execute(self):
        # Sanitize the input to prevent command injection
        if not self.host.isalnum():
            raise ValueError("Invalid host")
        command = ["ping", self.host]
        try:
            await asyncio.create_subprocess_exec(*command)
        except Exception as e:
            return str(e)

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    ping_command = PingCommand(host)
    result = ping_command.execute()
    return {"status": "completed", "result": result}