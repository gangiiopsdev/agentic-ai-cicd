from fastapi import FastAPI
import subprocess
class PingCommand:
    def __init__(self, host):
        self.host = host

    def run(self):
        if not isinstance(self.host, str) or not self.host.strip():
            raise ValueError('Invalid host provided')
        result = subprocess.run(['ping', self.host], capture_output=True, text=True, check=True)
        return result.stdout


global ping_command
ping_command = PingCommand(None)

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    try:
        result = subprocess.run(['ping', host], capture_output=True, text=True, check=True)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'error', 'message': str(e)}