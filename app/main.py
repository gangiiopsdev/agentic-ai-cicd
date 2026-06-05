from fastapi import FastAPI
import subprocess
class CommandRunner:
    def __init__(self, host):
        self.host = host

    async def run(self):
        cmd = ['ping', self.host]
        result = await asyncio.create_subprocess_exec(*cmd,
                                               stdout=subprocess.PIPE,
                                               stderr=subprocess.PIPE)
        return await result.communicate()

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    runner = CommandRunner(host)
    output, error = runner.run()
    return {"status": "completed", "output": output.decode(), "error": error.decode() if error else None}