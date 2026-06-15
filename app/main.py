from fastapi import FastAPI
import subprocess
class PingCommand:
    def __init__(self, host: str):
        self.host = host

    def run(self):
        try:
            # Use the shlex module to properly escape command arguments
            from shlex import quote
            subprocess.run(['ping', quote(self.host)], check=True)
        except subprocess.CalledProcessError as e:
            return {'error': f'Ping failed with error: {e}'}, 500

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    # Validate and sanitize the input before using it in the command
    if not host or not all(c.isalnum() for c in host):  # Basic validation, may need more complex checks depending on requirements
        return {'error': 'Invalid hostname'}, 400
    ping_command = PingCommand(host)
    result = ping_command.run()
    return result