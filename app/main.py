from fastapi import FastAPI
import subprocess
import shlex

class PingCommand:
    def __init__(self, host):
        self.host = host

    async def execute(self):
        cmd_parts = ['ping', shlex.quote(self.host)]
        try:
            result = await asyncio.to_thread(subprocess.run, cmd_parts, capture_output=True, text=True, check=True)
            return result.stdout
        except subprocess.CalledProcessError as e:
            return str(e)

class PingEndpoint:
    def __init__(self):
        self.ping_command = PingCommand()

    async def ping(self, host: str):
        try:
            response = await self.ping_command.execute()
            return {'status': 'completed', 'response': response}
        except Exception as e:
            return {'status': 'failed', 'error': str(e)}

app = FastAPI()
ping_endpoint = PingEndpoint()

@app.get(")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    return ping_endpoint.ping(host)