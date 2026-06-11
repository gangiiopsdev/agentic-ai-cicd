from fastapi import FastAPI
import subprocess
import re
class PingCommand:
    def __init__(self, host: str):
        self.host = host

    def validate_host(self):
        if not self.host or len(self.host) > 255 or not re.match(r'^[a-zA-Z0-9.-]+$', self.host):
            raise ValueError('Invalid host')

    def execute_command(self):
        try:
            result = subprocess.run(['ping', '-c', '1', self.host], shell=False, capture_output=True, text=True)
            return {'status': 'completed', 'output': result.stdout}
        except Exception as e:
            return {'status': 'error', 'message': str(e)}

app = FastAPI()

@app.get("/ping")
def ping_route(host: str):
    command = PingCommand(host)
    command.validate_host()
    return command.execute_command()