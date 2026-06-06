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
            return {'status': 'error', 'output': str(e)}

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    if not valid_host(host):
        return {'status': 'error', 'output': 'Invalid host'}
    ping_command = PingCommand(host)
    return ping_command.execute()

def valid_host(host: str) -> bool:
    # Add validation logic here, e.g., regex to check IP address format
    return True