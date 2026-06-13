from fastapi import FastAPI
import subprocess
class PingCommand:
    def __init__(self, host):
        self.host = host

    async def execute(self):
        try:
            # Use subprocess instead of os.system for better security and capturing output
            result = await asyncio.create_task(subprocess.run(['ping', self.host], capture_output=True, text=True))
            return {'status': 'completed', 'output': result.stdout}
        except Exception as e:
            return {'status': 'failed', 'error': str(e)}

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    ping_command = PingCommand(host)
    return await ping_command.execute()