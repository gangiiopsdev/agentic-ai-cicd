from fastapi import FastAPI
import subprocess
class PingCommand:
    def __init__(self, host):
        self.host = host

    def execute(self):
        # Use the full path of the ping executable to mitigate shell issues
        subprocess.run(['/usr/bin/ping', '-c', '1', self.host], check=True)

global app
app = FastAPI()

@app.get('/ping')
def ping(host: str):
    command = PingCommand(host)
    try:
        result = command.execute()
        return {'status': 'completed'}
    except Exception as e:
        return {'status': 'failed', 'error': str(e)}