from fastapi import FastAPI
import subprocess

# Define a list of allowed hosts for security reasons
ALLOWED_HOSTS = ['example.com', 'localhost']

class PingCommand:
    def __init__(self, host):
        self.host = host

    def execute(self):
        if self.host not in ALLOWED_HOSTS:
            return {'status': 'error', 'message': 'Invalid host'}
        try:
            result = subprocess.run(['ping', self.host], capture_output=True, text=True)
            return {'status': 'completed', 'output': result.stdout}
        except Exception as e:
            return {'status': 'error', 'message': str(e)}

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    # Validate host before using it
    if validate_host(host):
        ping_command = PingCommand(host)
        return ping_command.execute()