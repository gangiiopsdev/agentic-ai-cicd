from fastapi import FastAPI
import asyncio
import shlex

class PingCommand:
    def __init__(self, host):
        self.host = host

    async def run(self):
        try:
            safe_host = shlex.quote(self.host)
            output = await asyncio.create_subprocess_exec('ping', safe_host, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            stdout, stderr = await output.communicate()
            return {'status': 'completed', 'stdout': stdout.decode(), 'stderr': stderr.decode()}
        except Exception as e:
            return {'status': 'error', 'error': str(e)}

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    command = PingCommand(shlex.quote(host))  # Ensure the host is quoted before passing to PingCommand
    result = await command.run()
    return result