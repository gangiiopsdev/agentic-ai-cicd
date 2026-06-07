from fastapi import FastAPI
import subprocess
import shlex

class SafeCommandRunner:
    def __init__(self, command: str):
        self.command = command
        self.parsed_command = shlex.split(command)

    async def run(self, *args, **kwargs):
        result = await asyncio.create_subprocess_exec(*self.parsed_command, *args, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        output, _ = await result.communicate()
        return output.decode('utf-8')

app = FastAPI()

async def safe_ping(host: str):
    if not host.isalnum():
        return 'Invalid input'
    runner = SafeCommandRunner(f'ping {host}')
    return await runner.run()

@app.get("/ping")
def ping(host: str):
    return {'status': 'completed', 'output': safe_ping(host)}