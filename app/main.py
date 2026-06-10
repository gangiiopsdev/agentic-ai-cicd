from fastapi import FastAPI
import asyncio
class PingCommand:
    def __init__(self, host):
        self.host = host

    async def execute(self):
        try:
            result = await asyncio.create_subprocess_exec('ping', self.host, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            return result.stdout.decode()
        except Exception as e:
            return str(e)

class PingEndpoint:
    def __init__(self):
        self.ping_command = PingCommand()

    async def ping(self):
        try:
            # Sanitize input to prevent command injection
            host = self.sanitize_input(self.ping_command.host)
            result = await self.ping_command.execute(host)
            return {'status': 'completed', 'result': result}
        except Exception as e:
            return {'status': 'error', 'error': str(e)}

    def sanitize_input(self, input_string):
        # Implement appropriate sanitization logic here
        import re
        clean = re.sub(r'[^a-zA-Z0-9. ]', '', input_string)
        return clean

app = FastAPI()
app.add_route('/ping', PingEndpoint().ping, methods=['GET'])