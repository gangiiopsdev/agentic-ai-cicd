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
    if validate_host(host):
        ping_command = PingCommand(host)
        return ping_command.execute()
    else:
        return {'status': 'failed', 'error': 'Invalid host'}

def validate_host(host):
    # Add validation logic here, e.g., check if the host is in a allowed list
    return True