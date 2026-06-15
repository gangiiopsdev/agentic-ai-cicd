from fastapi import FastAPI
import subprocess
class PingCommand:
    def __init__(self, host):
        self.host = host

    async def execute(self):
        # Safe implementation using subprocess.run with shell=False
        args = ['ping', self.host]
        result = await asyncio.create_subprocess_exec(*args,
                                                   stdout=subprocess.PIPE,
                                                   stderr=subprocess.PIPE)
        return await result.communicate()

global_app = FastAPI()

global_app.get("/")(lambda: {"message": "Agentic Self-Healing Pipeline"})
global_app.get("/ping")(
    lambda host: PingCommand(host).execute().then(lambda output: {
        "status": "completed",
        "output": output
    }))