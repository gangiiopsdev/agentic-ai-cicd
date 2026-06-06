from fastapi import FastAPI
import subprocess
class PingCommand:
    def __init__(self, host: str):
        self.host = host
        self.args = ['ping', '-c', '1', host]

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    # Validate and sanitize the input to prevent injection attacks
    if not validate_host(host):
        return {'status': 'error', 'message': 'Invalid host'}
    command = PingCommand(host)
    result = subprocess.run(command.args, capture_output=True, text=True, check=False)
    return {'status': 'completed', 'output': result.stdout}
def validate_host(host: str) -> bool:
    # Implement a simple validation logic for the host
    import re
    pattern = r'^[a-zA-Z0-9.-]+$'
    return re.match(pattern, host) is not None