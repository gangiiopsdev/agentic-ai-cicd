from fastapi import FastAPI
import subprocess
class PingCommand:
    def __init__(self, host: str):
        self.host = host

    def validate_host(self):
        # Implement validation logic here to ensure the host is safe
        if not self.host.isalnum():
            raise ValueError('Invalid host name')

    def execute_command(self):
        try:
            result = subprocess.run(['ping', self.host], capture_output=True, text=True, check=True)
            return {'status': 'completed', 'output': result.stdout}
        except subprocess.CalledProcessError as e:
            return {'status': 'failed', 'error': e.stderr}

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    command = PingCommand(host)
    command.validate_host()
    return command.execute_command()