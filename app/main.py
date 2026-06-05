from fastapi import FastAPI
import subprocess
class PingCommand:
    def __init__(self, host):
        self.host = host

    def execute(self):
        try:
            result = subprocess.run(['ping', '-c', '1', self.host], capture_output=True, text=True, check=True)
            return {'status': 'completed', 'output': result.stdout}
        except subprocess.CalledProcessError as e:
            return {'status': 'failed', 'error': str(e)}

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    # Validate and sanitize host input before using it in the subprocess command.
    if not validate_host(host):
        return {'status': 'failed', 'error': 'Invalid host'}
    ping_command = PingCommand(host)
    return ping_command.execute()

# Example validation function (replace with actual validation logic)
def validate_host(host: str) -> bool:
    # Check if the host is a valid IP address or domain name
    import re
    pattern = re.compile(r'^[a-zA-Z0-9.-]+$')
    return pattern.match(host) is not None