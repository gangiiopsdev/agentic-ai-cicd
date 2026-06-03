from fastapi import FastAPI
import subprocess
class PingCommand:
    def __init__(self, host: str):
        self.host = host

    def execute(self) -> dict:
        try:
            output = subprocess.check_output(['ping', self.host], stderr=subprocess.STDOUT, timeout=5)
            return {'status': 'completed', 'output': output.decode()}
        except subprocess.CalledProcessError as e:
            return {'status': 'failed', 'error': e.output.decode()}

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    command = PingCommand(host)
    return command.execute()