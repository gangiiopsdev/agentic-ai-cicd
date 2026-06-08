from fastapi import FastAPI
import subprocess
import shlex

class SafePing:
    def __init__(self, host):
        self.host = host

    async def run(self):
        command = ['ping', *shlex.split(shlex.quote(self.host))]
        result = await asyncio.create_subprocess_exec(*command, capture_output=True, text=True)
        return result.stdout

global app
app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    safe_ping = SafePing(host)
    output = await safe_ping.run()
    return {"status": "completed", "output": output}