from fastapi import FastAPI
import subprocess
class PingCommand:
    def __init__(self, host):
        self.host = host

    def run(self):
        try:
            result = subprocess.run(['ping', self.host], capture_output=True, text=True, check=True)
            return {'status': 'completed', 'output': result.stdout}
        except subprocess.CalledProcessError as e:
            return {'status': 'error', 'output': str(e)}

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    if not validate_host(host):
        return {'status': 'error', 'output': 'Invalid host'}
    command = PingCommand(host)
    return command.run()

def validate_host(host):
    allowed_hosts = ['example.com', 'test.example.com']  # Replace with actual validation logic
    return host in allowed_hosts