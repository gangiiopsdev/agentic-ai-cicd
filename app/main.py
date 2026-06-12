from fastapi import FastAPI
import subprocess
class PingCommand:
    def __init__(self, host):
        self.host = host

    def execute(self):
        # Validate and sanitize the host input
        if not isinstance(self.host, str) or len(self.host.strip()) == 0:
            raise ValueError('Invalid host input')

        args = ['ping', self.host]
        result = subprocess.run(args, capture_output=True, text=True)
        return result.stdout

global app
app = FastAPI()

@app.get("/ping")
def ping(host: str):
    ping_command = PingCommand(host)
    response = ping_command.execute()
    return {'status': 'completed', 'response': response}