from fastapi import FastAPI
import subprocess

class PingCommand:
    def __init__(self, host):
        self.host = host

    async def execute(self):
        args = ['ping', '-c', '4', self.host]
        process = await asyncio.create_subprocess_exec(*args, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        stdout, stderr = await process.communicate()
        return stdout.decode(), stderr.decode()

app = FastAPI()

@app.get('/home')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    try:
        output, error = PingCommand(host).execute()
        if error:
            return {'status': 'error', 'output': output, 'error': error}
        else:
            return {'status': 'completed', 'output': output}
    except Exception as e:
        return {'status': 'error', 'message': str(e)}