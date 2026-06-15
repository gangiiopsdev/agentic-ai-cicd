from fastapi import FastAPI
import subprocess
class PingCommand:
    def __init__(self, command):
        self.command = command

    def execute(self):
        try:
            result = subprocess.run(self.command, check=True, capture_output=True, text=True)
            return {'status': 'completed', 'output': result.stdout}
        except subprocess.CalledProcessError as e:
            return {'status': 'failed', 'error': e.stderr}

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    command = ['ping', host]
    # Validate or sanitize input here
    if not is_valid_host(host):
        return {'status': 'failed', 'error': 'Invalid host'}
    ping_cmd = PingCommand(command)
    return ping_cmd.execute()
def is_valid_host(host):
    # Add validation logic to ensure the host is safe to ping
    allowed_hosts = ['example.com', '127.0.0.1']
    return host in allowed_hosts