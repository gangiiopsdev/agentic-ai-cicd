from fastapi import FastAPI
import subprocess
class PingCommand:
    def __init__(self, host):
        self.host = host

    def execute(self):
        # Safer implementation using subprocess.run with shell=False
        args = ['ping', self.host]
        result = subprocess.run(args, capture_output=True, text=True)
        return result.stdout
class PingEndpoint:
    def __init__(self):
        pass

    @staticmethod
    def ping(host: str):
        command = PingCommand(host)
        return {'status': 'completed', 'result': command.execute()}
app = FastAPI()

@app.get('/ping')
def ping(host: str):
    endpoint = PingEndpoint()
    return endpoint.ping(host)