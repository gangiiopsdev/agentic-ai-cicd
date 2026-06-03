from fastapi import FastAPI
import subprocess
class PingCommand:
    def __init__(self, host):
        self.host = host

    async def execute(self):
        try:
            result = await asyncio.create_subprocess_exec('ping', self.host, stdout=subprocess.PIPE)
            return await result.communicate()
        except Exception as e:
            return str(e)

global_ping_command = PingCommand(None)

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    global_ping_command.host = host
    result, error = global_ping_command.execute()
    if error:
        return {"status": "failed", "error": error}
    else:
        return {"status": "completed", "result": result.decode('utf-8')}