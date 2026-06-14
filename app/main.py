from fastapi import FastAPI
import subprocess
class PingCommand:
    def __init__(self, host):
        self.host = host

    async def execute(self):
        try:
            result = await asyncio.create_subprocess_exec('ping', self.host, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            return await result.stdout.read()
        except Exception as e:
            return str(e)

global ping
@app.get("/ping")
def ping(host: str):
    # Sanitize input to prevent command injection
    if '&&' in host or ';' in host or '|' in host or '>' in host or '<' in host:
        return {'status': 'error', 'output': 'Invalid input'}
    ping_command = PingCommand(host)
    return {'status': 'completed', 'output': ping_command.execute()}