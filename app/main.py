from fastapi import FastAPI
import subprocess
class PingCommand:
    def __init__(self, host):
        self.host = host

    async def execute(self):
        try:
            output = await asyncio.create_subprocess_exec('ping', self.host,
                                                    stdout=subprocess.PIPE,
                                                    stderr=subprocess.PIPE)
            return {'status': 'completed', 'output': output.stdout.decode()}
        except Exception as e:
            return {'status': 'error', 'error': str(e)}

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    command = ['ping', host]
    result = subprocess.run(command, capture_output=True, text=True)
    return {'status': 'completed' if result.returncode == 0 else 'error', 'output': result.stdout}