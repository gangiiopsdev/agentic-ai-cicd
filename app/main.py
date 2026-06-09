from fastapi import FastAPI
import subprocess
class PingCommand:
    def __init__(self, host):
        self.host = host

    async def execute(self):
        command = ['ping', '-c', '1', self.host]
        process = await asyncio.create_subprocess_exec(*command,
                                                       stdout=subprocess.PIPE,
                                                       stderr=subprocess.PIPE)
        stdout, stderr = await process.communicate()
        return stdout.decode(), stderr.decode()

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    sanitized_host = sanitize_input(host)
    command = PingCommand(sanitized_host)
    output, errors = command.execute()
    if errors:
        return {'status': 'failed', 'error': errors}
    else:
        return {'status': 'completed', 'output': output}