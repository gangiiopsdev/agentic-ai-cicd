from fastapi import FastAPI
import subprocess
class PingCommand:
    def __init__(self, host):
        self.host = host

    def execute(self):
        try:
            # Use a whitelist of allowed hosts or use a safer method to validate input
            if not any(host.endswith(suffix) for suffix in ['.com', '.org', '.net']):
                raise ValueError('Invalid host')
            result = subprocess.run(['ping', self.host], capture_output=True, text=True, check=True)
            return {'status': 'completed', 'output': result.stdout}
        except subprocess.CalledProcessError as e:
            return {'status': 'failed', 'error': str(e)}

app = FastAPI()

@app.get("/home")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Sanitize the input to prevent command injection
    if not any(host.endswith(suffix) for suffix in ['.com', '.org', '.net']):
        raise ValueError('Invalid host')
    command = PingCommand(host)
    return command.execute()