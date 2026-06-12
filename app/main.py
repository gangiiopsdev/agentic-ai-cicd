from fastapi import FastAPI
import subprocess

class PingCommand:
    def __init__(self, host: str):
        self.host = host

    def execute(self):
        try:
            result = subprocess.run(['/bin/ping', '-c', '1', self.host], capture_output=True, text=True, check=True)
            return {'status': 'completed', 'output': result.stdout}
        except subprocess.CalledProcessError as e:
            return {'status': 'failed', 'error': str(e)}

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    # Validate host input
    if not is_valid_host(host):
        return {'status': 'failed', 'error': 'Invalid host'}
    command = PingCommand(host)
    return command.execute()

def is_valid_host(host: str) -> bool:
    allowed_hosts = ['example.com', 'localhost']  # Example validation logic
    return host in allowed_hosts