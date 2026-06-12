from fastapi import FastAPI
import subprocess
import shlex

class PingCommand:
    def __init__(self, host):
        self.host = host

    async def execute(self):
        try:
            args = ['ping', '-c', '4'] + shlex.split(self.host)
            result = await asyncio.create_subprocess_exec(*args, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            output, error = await result.communicate()
            if result.returncode == 0:
                return {'status': 'completed', 'output': output.decode()}
            else:
                return {'status': 'failed', 'error': error.decode()}
        except Exception as e:
            return {'status': 'failed', 'error': str(e)}

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    ping_command = PingCommand(host)
    return await ping_command.execute()