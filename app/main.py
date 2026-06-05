from fastapi import FastAPI
import subprocess
class PingCommand:
    def __init__(self, host: str):
        self.host = host
        self.args = ['ping', '-c', '1', host]

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    command = PingCommand(host)
    result = subprocess.run(command.args, capture_output=True, text=True, check=False)
    return {'status': 'completed', 'output': result.stdout}