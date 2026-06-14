from fastapi import FastAPI
import subprocess
class PingCommand:
    def __init__(self, host):
        self.host = host

    def execute(self):
        try:
            result = subprocess.run(['ping', '-c', '1', self.host], capture_output=True, text=True, check=True)
            return {'status': 'completed', 'output': result.stdout}
        except Exception as e:
            return {'status': 'failed', 'error': str(e)}

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    if not is_valid_host(host):
        return {'status': 'failed', 'error': 'Invalid host'}
    ping_command = PingCommand(host)
    return ping_command.execute()

def is_valid_host(host):
    # Add validation logic here, e.g., regex to allow only certain IP addresses or domain names
    import re
    pattern = r'^[a-zA-Z0-9.-]+$'
    if not re.match(pattern, host):
        return False
    return True