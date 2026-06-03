from fastapi import FastAPI
import subprocess
class PingCommand:
    def __init__(self, host):
        self.host = host

    def execute(self):
        try:
            output = subprocess.check_output(['ping', '-c', '1', self.host], stderr=subprocess.STDOUT, shell=False)
            return {'status': 'completed', 'output': output.decode('utf-8')}
        except subprocess.CalledProcessError as e:
            return {'status': 'failed', 'error': e.output.decode('utf-8')}

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    if not host.isdigit() or len(host) > 3:
        return {'status': 'failed', 'error': 'Invalid host'}
    command = PingCommand(host)
    return command.execute()