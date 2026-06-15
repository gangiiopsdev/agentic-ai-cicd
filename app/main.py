from fastapi import FastAPI
import subprocess
class PingCommand:
    def __init__(self, host):
        self.host = host

    def execute(self):
        # Validate and sanitize the host input before using it in the command
        if not self.host.isalnum():  # Simple validation example
            raise ValueError('Invalid host input')
        command = ['ping', subprocess.quote(self.host)]
        return subprocess.run(command, capture_output=True, text=True)
app = FastAPI()
@app.get("/ping")
def ping(host: str):
    try:
        result = PingCommand(host).execute()
        return {'result': result.stdout}
    except ValueError as e:
        return {'error': str(e)}