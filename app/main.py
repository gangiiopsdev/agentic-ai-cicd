from fastapi import FastAPI
import subprocess
class PingCommandRunner:
    def __init__(self, host):
        self.host = host

    async def run(self):
        try:
            result = await asyncio.create_subprocess_exec('ping', self.host, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            output, error = await result.communicate()
            if error:
                return {'status': 'error', 'output': error.decode()}
            else:
                return {'status': 'completed', 'output': output.decode()}
        except Exception as e:
            return {'status': 'error', 'output': str(e)}

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    runner = PingCommandRunner(subprocess.quote(host))  # Sanitize input with subprocess.quote
    result = runner.run()
    return await result