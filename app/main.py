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
            return {'status': 'error', 'output': str(e)}

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    # Validate the host to ensure it only contains allowed characters (e.g., alphanumeric, hyphen, dot)
    if not re.match(r'^[a-zA-Z0-9-.]+$', host):
        return {'status': 'error', 'output': 'Invalid host'}
    ping_command = PingCommand(host)
    return ping_command.execute()