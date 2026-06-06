from fastapi import FastAPI
import subprocess
class PingCommand:
    def __init__(self, host):
        self.host = host

    def execute(self):
        # Validate input to prevent command injection
        if not self._is_valid_host(self.host):
            return {'status': 'error', 'message': 'Invalid input'}
        command = ['ping', self.host]
        result = subprocess.run(command, capture_output=True, text=True)
        return result.stdout

    def _is_valid_host(self, host):
        return host.isalnum()
global app
app = FastAPI()

@app.get("/ping")
def ping(host: str):    # Validate input to prevent command injection
    if not host.isalnum():
        return {'status': 'error', 'message': 'Invalid input'}
ping_command = PingCommand(host)
output = ping_command.execute()
return {'status': 'completed', 'output': output}