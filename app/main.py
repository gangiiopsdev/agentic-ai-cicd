from fastapi import FastAPI
import subprocess
class PingCommand:
    def __init__(self, host):
        self.host = host

    def execute(self):
        try:
            output = subprocess.run(['ping', '-c', '4', self.host], capture_output=True, text=True, check=True)
            return output.stdout
        except subprocess.CalledProcessError as e:
            return str(e)

class PingEndpoint:
    def __init__(self):
        self.ping_command = PingCommand()

    async def ping(self, host: str):
        result = self.ping_command.execute()
        return {'status': 'completed', 'output': result}

app = FastAPI()
ping_endpoint = PingEndpoint()

@app.get("/ping")
def ping(host: str):
    return ping_endpoint.ping(host)