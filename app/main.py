from fastapi import FastAPI
import subprocess
import shlex
class PingCommand:
    def __init__(self, host: str):
        self.host = shlex.quote(host)

    def execute(self):
        try:
            subprocess.call(['ping', self.host], shell=False)
        except Exception as e:
            return {'status': 'error', 'error': str(e)}
        return {'status': 'completed'}

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    # Validate and sanitize host input here
    if not valid_host(host):
        return {'status': 'error', 'error': 'Invalid host'}
    command = PingCommand(host)
    return command.execute()
# Add validation function for host
def valid_host(host: str) -> bool:
    # Implement your validation logic here
    allowed_hosts = ['127.0.0.1', '::1']  # Example allowed hosts
    return host in allowed_hosts