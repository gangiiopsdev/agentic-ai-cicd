from fastapi import FastAPI
import subprocess
class PingCommand:
    def __init__(self, host):
        self.host = host

    async def run(self):
        try:
            result = await asyncio.create_subprocess_exec('ping', self.host, capture_output=True, text=True)
            return {'status': 'completed', 'output': result.stdout}
        except Exception as e:
            return {'status': 'error', 'message': str(e)}

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    ping_command = PingCommand(host)
    return await ping_command.run()