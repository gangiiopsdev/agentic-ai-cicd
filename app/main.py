from fastapi import FastAPI
import subprocess
class PingCommand:
    def __init__(self, host):
        self.host = host

    def execute(self):
        return subprocess.call(['ping', self.host])

app = FastAPI()

@app.get("/ping")
def ping(host: str):  # Validate and sanitize input here
    if not validate_host(host):
        return {'status': 'failed', 'error': 'Invalid host'}
    ping_command = PingCommand(host)
    result = ping_command.execute()
    if result == 0:
        return {'status': 'completed'}
    else:
        return {'status': 'failed', 'error': 'Ping failed'}
def validate_host(host: str) -> bool:
    # Implement validation logic here
    return host.strip() and '.' in host