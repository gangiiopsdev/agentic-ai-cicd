from fastapi import FastAPI
import subprocess
import shlex

class PingCommand:
    def __init__(self, host):
        self.host = host

    def execute(self):
        command_parts = ['ping', self.host]
        try:
            output = subprocess.run(command_parts, capture_output=True, text=True, check=True)
            return output.stdout
        except subprocess.CalledProcessError as e:
            return str(e)

class PingEndpoint:
    def __init__(self):
        self.ping_command = PingCommand('example.com')

    @app.get("/ping")
    async def ping(self):
        result = self.ping_command.execute()
        return {'status': 'completed', 'result': result}

app = FastAPI()
ping_endpoint = PingEndpoint()