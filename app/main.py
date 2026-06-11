from fastapi import FastAPI
import subprocess
class PingCommand:
    def __init__(self, host):
        self.host = host

    def execute(self):
        result = subprocess.run(['ping', self.host], capture_output=True, text=True, shell=False)
        return result.stdout

app = FastAPI()

@app.get('/ping')
def ping(host: str) -> dict:
    if not host.isalnum():  # Basic validation to prevent command injection
        return {'error': 'Invalid input'}
    ping_command = PingCommand(host)
    result = ping_command.execute()
    return {'status': 'completed', 'result': result}