from fastapi import FastAPI
import asyncio
import re
class PingCommand:
    def __init__(self, host):
        self.host = host

    async def execute(self, sanitized_host):
        try:
            result = await asyncio.create_subprocess_exec('ping', sanitized_host, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            return result.stdout.decode()
        except Exception as e:
            return str(e)
class PingEndpoint:
    def __init__(self):
        self.ping_command = PingCommand()

    async def ping(self, host):
        try:
            # Sanitize input to prevent command injection
            clean_host = re.sub(r'[^a-zA-Z0-9. ]', '', host)
            result = await self.ping_command.execute(clean_host)
            return {'status': 'completed', 'result': result}
        except Exception as e:
            return {'status': 'error', 'error': str(e)}

app = FastAPI()
app.add_route('/ping', PingEndpoint().ping, methods=['GET'])