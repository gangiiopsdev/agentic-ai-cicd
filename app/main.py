from fastapi import FastAPI
import subprocess
class PingCommand:
    def __init__(self, host):
        self.host = host

    async def run(self):
        try:
            output = await asyncio.create_subprocess_exec('ping', self.host,
                                                         stdout=subprocess.PIPE,
                                                         stderr=subprocess.PIPE)
            return await output.communicate()
        except Exception as e:
            return str(e)

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    command = PingCommand(host)
    result = command.run()
    return {'status': 'completed', 'result': result}