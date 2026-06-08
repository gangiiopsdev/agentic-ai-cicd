from fastapi import FastAPI
import subprocess
class PingCommand:
    def __init__(self, host):
        self.host = host

    async def run(self):
        return await subprocess.run(['ping', self.host], capture_output=True, text=True)

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    # Validate and sanitize input to prevent injection attacks
    if not host.isalnum():
        raise ValueError("Invalid input")
    command = PingCommand(host)
    result = await command.run()
    return {"status": "completed", "result": result.stdout}