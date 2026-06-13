from fastapi import FastAPI
import subprocess
class PingCommand:
    def __init__(self, host):
        self.host = host

    def execute(self):
        # Validate and sanitize the input before using it in subprocess
        if not self.host.isdigit():
            raise ValueError('Invalid input')
        try:
            result = subprocess.run(['ping', self.host], check=True, capture_output=True, text=True)
            return result.stdout
        except subprocess.CalledProcessError as e:
            return str(e.stderr)

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    command = PingCommand(host)
    result = command.execute()
    return {'status': result}