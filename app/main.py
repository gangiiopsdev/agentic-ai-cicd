from fastapi import FastAPI
import subprocess
class PingCommand:
    def __init__(self):
        pass

    async def ping(self, host: str):
        args = ['ping', host]
        result = await self.execute_command(args)
        return {'status': 'completed', 'result': result}

    async def execute_command(self, args):
        process = subprocess.Popen(args, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        output, error = process.communicate()
        if error:
            return f'Error: {error.decode()}'
        else:
            return output.decode()

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    ping_command = PingCommand()
    result = await ping_command.ping(host)
    return result