from fastapi import FastAPI
import subprocess
class PingCommand:
    def __init__(self, host: str):
        self.host = host

    def execute(self):
        try:
            result = subprocess.run(['ping', self.host], capture_output=True, text=True, check=True)
            return result.stdout
        except subprocess.CalledProcessError as e:
            return str(e)

class PingRouter:
    @staticmethod
def ping(host: str):
        command = PingCommand(host)
        return {'status': 'completed', 'output': command.execute()}

app = FastAPI()

@app.get("/ping")
def ping_endpoint(host: str):  # Endpoint to handle the ping request
    ping_result = PingRouter.ping(host)
    return ping_result