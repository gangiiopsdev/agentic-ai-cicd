from fastapi import FastAPI
import subprocess
class PingCommand:
    def __init__(self, host):
        self.host = host

    def execute(self):
        try:
            output = subprocess.check_output(['ping', self.host], stderr=subprocess.STDOUT)
            return {'status': 'completed', 'output': output.decode()}
        except subprocess.CalledProcessError as e:
            return {'status': 'failed', 'error': e.output.decode()}

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    # Validate the host input to prevent command injection
    if not validate_host(host):
        return {'status': 'failed', 'error': 'Invalid host'}
    ping_command = PingCommand(host)
    return ping_command.execute()

# Function to validate the host input
def validate_host(host: str) -> bool:
    # Implement validation logic here, e.g., checking for allowed characters or formats
    return all(c.isalnum() or c in '.-' for c in host)