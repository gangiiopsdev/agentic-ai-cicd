from fastapi import FastAPI
import subprocess
class PingCommand:
    def __init__(self, host: str):
        self.host = host

    def execute(self) -> None:
        args = ['ping', self.host]
        subprocess.run(args, check=True)

class PingEndpoint:
    @staticmethod
def ping(host: str) -> dict:
        ping_command = PingCommand(host)
        try:
            ping_command.execute()
        except subprocess.CalledProcessError as e:
            return {'error': 'Failed to execute ping command', 'details': str(e)}

app = FastAPI()

@app.get("/ping")
def ping_endpoint(host: str) -> dict:
    return PingEndpoint.ping(host)