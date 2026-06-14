from fastapi import FastAPI
import subprocess
class PingCommand:
    def __init__(self, host):
        self.host = host

    def execute(self):
        try:
            result = subprocess.run(['/bin/ping', self.host], capture_output=True, text=True, check=True)
            return result.stdout
        except subprocess.CalledProcessError as e:
            return str(e)
class PingEndpoint:
    def __init__(self, app):
        @app.get("/ping")
        async def ping(self, host: str):
            command = PingCommand(host)
            return {'status': 'completed', 'result': command.execute()}

app = FastAPI()
ping_endpoint = PingEndpoint(app)