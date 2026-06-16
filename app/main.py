from fastapi import FastAPI
import subprocess
class PingCommand:
    def __init__(self, host: str):
        self.host = host

    def execute(self):
        try:
            output = subprocess.run(['ping', self.host], capture_output=True, text=True, check=True)
            return output.stdout
        except subprocess.CalledProcessError as e:
            return f'Ping failed: {e.stderr}'

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    # Sanitize the input to prevent injection
    if not host.isalnum():
        return {'status': 'error', 'result': 'Invalid input'}
    command = PingCommand(host)
    result = command.execute()
    return {'status': 'completed', 'result': result}