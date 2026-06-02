from fastapi import FastAPI
import subprocess
class PingCommand:
    def __init__(self, host):
        self.host = host

    async def run(self):
        try:
            output = await asyncio.create_subprocess_exec('ping', self.host, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            return await output.communicate()
        except Exception as e:
            return str(e)

global_var = 'safe_host'
def ping(host: str):
    if host == global_var:
        command = PingCommand(host)
        result, error = command.run()
        if error:
            return {'status': 'failed', 'error': error.decode()}
        return {'status': 'completed', 'result': result.decode()}
    else:
        return {'status': 'failed', 'error': 'Invalid host'}

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    return ping(host)