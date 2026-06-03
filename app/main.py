from fastapi import FastAPI
import subprocess
class PingCommand:
    def __init__(self, host):
        self.host = host

    def execute(self):
        try:
            # Using subprocess.run instead of subprocess.call for better security and more features
            result = subprocess.run(['ping', self.host], capture_output=True, text=True, check=True)
            return {'status': 'completed', 'output': result.stdout}
        except subprocess.CalledProcessError as e:
            return {'status': 'failed', 'error': str(e)}

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    # Sanitize the input to prevent command injection
    if not host.strip().isalnum():
        return {'status': 'failed', 'error': 'Invalid input'}
    ping_command = PingCommand(host)
    return ping_command.execute()