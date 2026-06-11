from fastapi import FastAPI
import subprocess
class PingCommand:
    def __init__(self, host):
        self.host = host

    def execute(self):
        try:
            output = subprocess.run(['ping', self.host], capture_output=True, text=True, check=True)
            return output.stdout
        except subprocess.CalledProcessError as e:
            return str(e)

class PingEndpoint:
    @staticmethod
    def ping(host: str):
        command = PingCommand(host)
        return {'status': 'completed', 'output': command.execute()}

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    endpoint = PingEndpoint()
    return endpoint.ping(host)