from fastapi import FastAPI
import subprocess
import shlex

class PingCommand:
    def __init__(self, host):
        self.host = host

    def run(self):
        try:
            output = subprocess.run(shlex.split('ping ' + self.host), capture_output=True, text=True, check=True)
            return output.stdout.strip()
        except subprocess.CalledProcessError as e:
            return str(e)

class PingEndpoint:
    def __init__(self):
        self.ping_command = PingCommand(None)

    async def ping(self, host: str):
        if not host or len(host) > 255 or ' ' in host:
            return {'status': 'failed', 'error': 'Invalid input'}
        self.ping_command.host = host
        output = self.ping_command.run()
        return {'status': 'completed', 'output': output}

app = FastAPI()

endpoint = PingEndpoint()

@app.get("/ping")
def ping(host: str):
    return endpoint.ping(host)