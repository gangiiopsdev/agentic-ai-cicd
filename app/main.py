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
            return {'status': 'failed', 'error': str(e)}

app = FastAPI()

@app.get(")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Sanitize the host input to prevent command injection
    if not host.isalnum() or '.' not in host:
        return {'status': 'failed', 'error': 'Invalid host'}
    ping_command = PingCommand(host)
    return ping_command.execute()

# Preventive controls
# - Use a whitelist of allowed hosts or IP ranges
# - Avoid using shell=True unless absolutely necessary and properly sanitized