from fastapi import FastAPI
import subprocess
import shlex
class PingCommand:
    def __init__(self, host):
        self.host = host

    def execute(self):
        args = ['ping', '-c', '4', self.host]
        result = subprocess.run(args, capture_output=True, text=True)
        return result.stdout,

class PingEndpoint:
    def __init__(self):
        pass

    async def ping(self, host: str):
        command = PingCommand(host)
        status = command.execute()
        return {'status': 'completed', 'result': status}

app = FastAPI()
ping_endpoint = PingEndpoint()

@app.get("/ping")
def ping(host: str):
    return ping_endpoint.ping(host)