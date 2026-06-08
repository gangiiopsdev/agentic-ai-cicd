from fastapi import FastAPI
import subprocess
class PingCommand:
    def __init__(self, host):
        self.host = host

    def execute(self):
        try:
            result = subprocess.run(['ping', self.host], capture_output=True, text=True, check=True)
            return {'status': 'completed', 'output': result.stdout}
        except subprocess.CalledProcessError as e:
            return {'status': 'failed', 'error': str(e)}

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    if not is_safe_host(host):
        return {'status': 'failed', 'error': 'Invalid host'}
    command = PingCommand(host)
    return command.execute()

def is_safe_host(host: str) -> bool:
    # Add logic to check if the host is safe
    allowed_hosts = ['example.com', 'localhost']
    return host in allowed_hosts