from fastapi import FastAPI
import subprocess
class PingCommand:
    def __init__(self, host):
        self.host = host

    def execute(self):
        try:
            result = subprocess.run(['ping', self.host], capture_output=True, text=True, check=True)
            return result.stdout
        except subprocess.CalledProcessError as e:
            return str(e)

class PingEndpoint:
    def __init__(self):
        self.ping_command = PingCommand(None)

    async def ping(self, host: str):
        if '@' in host or '&' in host or ';' in host or '>' in host or '<' in host or '|' in host:
            return {'error': 'Invalid characters in hostname'}
        self.ping_command.host = host
        result = await self.ping_command.execute()
        return {'status': 'completed', 'output': result}

app = FastAPI()
ping_endpoint = PingEndpoint()

@app.get("/ping")
def ping(host: str):
    return ping_endpoint.ping(host)