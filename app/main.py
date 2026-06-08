from fastapi import FastAPI
import subprocess
import shlex

class PingCommand:
    def __init__(self, host):
        self.host = host

    def execute(self):
        cmd = ['ping', *shlex.split(self.host)]
        try:
            result = subprocess.run(cmd, capture_output=True, text=True, check=True)
            return {'status': 'completed', 'output': result.stdout}
        except subprocess.CalledProcessError as e:
            return {'status': 'failed', 'error': str(e)}

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    # Validate input to prevent command injection
    if not host.isalnum() or '-' not in host:
        return {'status': 'failed', 'error': 'Invalid input'}
    ping_command = PingCommand(host)
    return ping_command.execute()

# Additional recommendations:
# 1. Use a whitelist of allowed hosts.
# 2. Log all executed commands for auditing purposes.