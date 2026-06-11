from fastapi import FastAPI
import subprocess
class PingCommand:
    def __init__(self, host: str):
        self.host = host

    async def execute(self):
        try:
            result = await asyncio.subprocess.create_subprocess_exec('ping', self.host, stdout=asyncio.subprocess.PIPE, stderr=asyncio.subprocess.PIPE)
            stdout, stderr = await result.communicate()
            if result.returncode != 0:
                raise subprocess.CalledProcessError(result.returncode, 'ping', stderr.decode())
            return {'status': 'completed', 'output': stdout.decode()}
        except subprocess.CalledProcessError as e:
            return {'status': 'failed', 'error': e.stderr.decode()}

app = FastAPI()

@app.get(")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    if host not in ['127.0.0.1', '::1']:  # Allow only localhost for security reasons
        return {'status': 'failed', 'error': 'Invalid host'}
    command = PingCommand(host)
    return await command.execute()