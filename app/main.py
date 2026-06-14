from fastapi import FastAPI
import subprocess
class PingCommand:
    def __init__(self, host):
        self.host = host

    def execute(self):
        try:
            # Using subprocess.run for better control and security
            subprocess.run(['ping', self.host], check=True, capture_output=True, text=True)
            return {'status': 'completed'}
        except subprocess.CalledProcessError as e:
            return {'status': 'failed', 'error': str(e)}

app = FastAPI()

@app.get="/ping")
def ping(host: str):
    ping_command = PingCommand(host)
    return ping_command.execute()