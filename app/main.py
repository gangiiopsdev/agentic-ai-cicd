from fastapi import FastAPI
import subprocess
import shlex
class PingCommand:
    def __init__(self, host):
        self.host = host

    async def execute(self):
        command = ['ping', shlex.quote(self.host)]
        process = await asyncio.create_subprocess_exec(*command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        output, error = await process.communicate()
        return output.decode(), error.decode()

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    command = PingCommand(host)
    output, error = await command.execute()
    if error:
        return {"status": "failed", "error": error}
    else:
        return {"status": "completed", "output": output}